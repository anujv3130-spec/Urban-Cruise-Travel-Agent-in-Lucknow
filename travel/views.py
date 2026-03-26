from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Avg, Count, Sum
from django.http import JsonResponse
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Destination, Tour, Booking, Review, Testimonial
from .forms import BookingForm, ReviewForm


def home(request):
    featured_destinations = Destination.objects.filter(featured=True)[:3]
    popular_tours = Tour.objects.filter(featured=True)[:6]
    testimonials = Testimonial.objects.filter(featured=True)[:3]
    
    context = {
        'featured_destinations': featured_destinations,
        'popular_tours': popular_tours,
        'testimonials': testimonials,
    }
    return render(request, 'travel/home.html', context)


def destinations(request):
    destinations_list = Destination.objects.all()
    countries = Destination.objects.values_list('country', flat=True).distinct()
    
    # Search functionality
    search_query = request.GET.get('search', '')
    country_filter = request.GET.get('country', '')
    
    if search_query:
        destinations_list = destinations_list.filter(
            Q(name__icontains=search_query) | Q(description__icontains=search_query)
        )
    
    if country_filter:
        destinations_list = destinations_list.filter(country=country_filter)
    
    paginator = Paginator(destinations_list, 9)
    page_number = request.GET.get('page')
    destinations = paginator.get_page(page_number)
    
    context = {
        'destinations': destinations,
        'countries': countries,
        'search_query': search_query,
        'selected_country': country_filter,
    }
    return render(request, 'travel/destinations.html', context)


def tours(request):
    tours_list = Tour.objects.all()
    
    # Filters
    tour_type = request.GET.get('type', '')
    duration = request.GET.get('duration', '')
    price_range = request.GET.get('price', '')
    search_query = request.GET.get('search', '')
    
    if tour_type:
        tours_list = tours_list.filter(tour_type=tour_type)
    
    if duration:
        if duration == '1':
            tours_list = tours_list.filter(duration=1)
        elif duration == '2-3':
            tours_list = tours_list.filter(duration__in=[2, 3])
        elif duration == '7':
            tours_list = tours_list.filter(duration=7)
        elif duration == '14+':
            tours_list = tours_list.filter(duration__gte=14)
    
    if price_range:
        if price_range == '0-500':
            tours_list = tours_list.filter(price__lt=500)
        elif price_range == '500-1000':
            tours_list = tours_list.filter(price__gte=500, price__lt=1000)
        elif price_range == '1000-2000':
            tours_list = tours_list.filter(price__gte=1000, price__lt=2000)
        elif price_range == '2000+':
            tours_list = tours_list.filter(price__gte=2000)
    
    if search_query:
        tours_list = tours_list.filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query) |
            Q(destination__name__icontains=search_query)
        )
    
    # Get tour types for filter dropdown
    tour_types = Tour.TOUR_TYPES
    
    paginator = Paginator(tours_list, 9)
    page_number = request.GET.get('page')
    tours = paginator.get_page(page_number)
    
    context = {
        'tours': tours,
        'tour_types': tour_types,
        'is_paginated': paginator.num_pages > 1,
    }
    return render(request, 'travel/tours.html', context)


def tour_detail(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    reviews = tour.reviews.all().order_by('-created_at')
    
    # Calculate average rating
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    
    context = {
        'tour': tour,
        'reviews': reviews,
        'avg_rating': avg_rating,
    }
    return render(request, 'travel/tour_detail.html', context)


@login_required
def book_tour(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.tour = tour
            booking.total_price = tour.price * booking.travelers_count
            booking.save()
            
            messages.success(request, f'Your booking for {tour.title} has been confirmed!')
            return redirect('my_bookings')
    else:
        form = BookingForm()
    
    return redirect('tour_detail', tour_id=tour_id)


@login_required
def add_review(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.tour = tour
            review.save()
            
            messages.success(request, 'Your review has been submitted!')
            return redirect('tour_detail', tour_id=tour_id)
    
    return redirect('tour_detail', tour_id=tour_id)


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    return render(request, 'travel/my_bookings.html', {'bookings': bookings})


@login_required
def cancel_booking(request, booking_id):
    """
    Cancel a booking and update its status
    """
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if booking.status != 'pending':
        messages.error(request, 'Only pending bookings can be cancelled.')
        return redirect('my_bookings')
    
    if request.method == 'POST':
        booking.status = 'cancelled'
        booking.save()
        messages.success(request, f'Booking for {booking.tour.title} has been cancelled successfully.')
        return redirect('my_bookings')
    
    return redirect('my_bookings')


@login_required
def profile(request):
    """
    Handle user profile viewing and updating
    """
    if request.method == 'POST':
        # Handle profile update
        user = request.user
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.email = request.POST.get('email', '')
        
        # Handle password change if provided
        current_password = request.POST.get('current_password', '')
        new_password = request.POST.get('new_password', '')
        confirm_password = request.POST.get('confirm_password', '')
        
        if current_password and new_password:
            if user.check_password(current_password):
                if new_password == confirm_password:
                    user.set_password(new_password)
                    messages.success(request, 'Profile and password updated successfully!')
                else:
                    messages.error(request, 'New passwords do not match!')
                    return render(request, 'travel/profile.html')
            else:
                messages.error(request, 'Current password is incorrect!')
                return render(request, 'travel/profile.html')
        else:
            messages.success(request, 'Profile updated successfully!')
        
        user.save()
        return redirect('profile')
    
    return render(request, 'travel/profile.html')


@login_required
def download_ticket(request, booking_id):
    """
    Generate and download a PDF ticket for a booking
    """
    from django.http import HttpResponse
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib import colors
    from reportlab.lib.units import inch
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from io import BytesIO
    from datetime import datetime
    import os
    
    # Get the booking
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    # Create a PDF
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    
    # Use default font
    font_name = 'Helvetica'
    
    # Header
    p.setFont(font_name, 24)
    p.setFillColor(colors.darkblue)
    p.drawString(50, height - 50, "URBAN CRUISE")
    
    p.setFont(font_name, 18)
    p.setFillColor(colors.black)
    p.drawString(50, height - 90, "TRAVEL TICKET")
    
    # Ticket border
    p.setStrokeColor(colors.darkblue)
    p.setLineWidth(2)
    p.rect(40, height - 120, width - 80, height - 200)
    
    # Booking Information
    p.setFont(font_name, 14)
    p.setFillColor(colors.black)
    y_position = height - 140
    
    p.drawString(60, y_position, f"Booking ID: URC{booking.id:06d}")
    y_position -= 25
    
    p.drawString(60, y_position, f"Tour: {booking.tour.title}")
    y_position -= 25
    
    p.drawString(60, y_position, f"Destination: {booking.tour.destination.name}")
    y_position -= 25
    
    p.drawString(60, y_position, f"Travelers: {booking.travelers_count}")
    y_position -= 25
    
    p.drawString(60, y_position, f"Duration: {booking.tour.duration} days")
    y_position -= 25
    
    p.drawString(60, y_position, f"Total Price: INR {booking.total_price:,}")
    y_position -= 25
    
    p.drawString(60, y_position, f"Booking Date: {booking.booking_date.strftime('%d %b %Y')}")
    y_position -= 25
    
    p.drawString(60, y_position, f"Status: {booking.get_status_display().title()}")
    y_position -= 40
    
    # Customer Information
    p.setFont(font_name, 16)
    p.setFillColor(colors.darkblue)
    p.drawString(60, y_position, "CUSTOMER INFORMATION")
    y_position -= 30
    
    p.setFont(font_name, 14)
    p.setFillColor(colors.black)
    p.drawString(60, y_position, f"Name: {booking.user.get_full_name() or booking.user.username}")
    y_position -= 25
    
    p.drawString(60, y_position, f"Email: {booking.contact_email}")
    y_position -= 25
    
    p.drawString(60, y_position, f"Phone: {booking.contact_phone}")
    y_position -= 40
    
    # Contact Information
    p.setFont(font_name, 16)
    p.setFillColor(colors.darkblue)
    p.drawString(60, y_position, "CONTACT INFORMATION")
    y_position -= 30
    
    p.setFont(font_name, 14)
    p.setFillColor(colors.black)
    p.drawString(60, y_position, "URBAN CRUISE Travel Services")
    y_position -= 25
    
    p.drawString(60, y_position, "6/486, Vineet Khand 6, Gomti Nagar")
    y_position -= 25
    
    p.drawString(60, y_position, "Lucknow, Uttar Pradesh 226010")
    y_position -= 25
    
    p.drawString(60, y_position, "Phone: +91 9260994765")
    y_position -= 25
    
    p.drawString(60, y_position, "Email: info@urbancruise.com")
    y_position -= 40
    
    # Important Notes
    p.setFont(font_name, 12)
    p.setFillColor(colors.red)
    p.drawString(60, y_position, "IMPORTANT NOTES:")
    y_position -= 20
    
    p.setFillColor(colors.black)
    notes = [
        "• Please carry this ticket and valid ID proof during travel",
        "• Report at the meeting point 15 minutes before departure",
        "• This ticket is non-transferable and non-refundable",
        "• For any queries, contact our 24/7 helpline"
    ]
    
    for note in notes:
        p.drawString(60, y_position, note)
        y_position -= 20
    
    # Footer
    p.setFont(font_name, 10)
    p.setFillColor(colors.gray)
    p.drawString(50, 30, f"Generated on {datetime.now().strftime('%d %b %Y %H:%M')}")
    p.drawString(width - 150, 30, "www.urbancruise.com")
    
    # Save the PDF
    p.save()
    
    # File response
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="URBAN_CRUISE_Ticket_{booking.id:06d}.pdf"'
    
    return response


def about(request):
    return render(request, 'travel/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Here you would typically send an email or save to database
        messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
        return redirect('contact')
    
    return render(request, 'travel/contact.html')


def services(request):
    """
    Display all services offered by URBAN CRUISE
    """
    return render(request, 'travel/services.html')


def login_view(request):
    """
    Handle user login
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Update user with additional fields
            user.first_name = request.POST.get('first_name', '')
            user.last_name = request.POST.get('last_name', '')
            user.email = request.POST.get('email', '')
            user.save()
            login(request, user)
            messages.success(request, 'Account created successfully! Welcome to URBAN CRUISE!')
            return redirect('home')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/signup.html', {'form': form})
