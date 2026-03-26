from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('destinations/', views.destinations, name='destinations'),
    path('tours/', views.tours, name='tours'),
    path('tour/<int:tour_id>/', views.tour_detail, name='tour_detail'),
    path('book/<int:tour_id>/', views.book_tour, name='book_tour'),
    path('review/<int:tour_id>/', views.add_review, name='add_review'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('profile/', views.profile, name='profile'),
    path('download-ticket/<int:booking_id>/', views.download_ticket, name='download_ticket'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
]
