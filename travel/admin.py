from django.contrib import admin
from .models import Destination, Tour, Booking, Review, Testimonial


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'featured', 'created_at']
    list_filter = ['country', 'featured', 'created_at']
    search_fields = ['name', 'country', 'description']
    list_editable = ['featured']
    readonly_fields = ['created_at']


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ['title', 'destination', 'tour_type', 'duration', 'price', 'max_travelers', 'featured']
    list_filter = ['tour_type', 'duration', 'featured', 'created_at']
    search_fields = ['title', 'description', 'destination__name']
    list_editable = ['featured']
    readonly_fields = ['created_at', 'updated_at']
    
    def available_spots(self, obj):
        return obj.available_spots
    available_spots.short_description = 'Available Spots'


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'tour', 'travelers_count', 'total_price', 'status', 'booking_date']
    list_filter = ['status', 'booking_date', 'tour__destination']
    search_fields = ['user__username', 'tour__title', 'contact_email']
    list_editable = ['status']
    readonly_fields = ['booking_date', 'total_price']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'tour', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['user__username', 'tour__title', 'comment']
    readonly_fields = ['created_at']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'featured', 'created_at']
    list_filter = ['featured', 'created_at']
    search_fields = ['name', 'message']
    list_editable = ['featured']
    readonly_fields = ['created_at']
