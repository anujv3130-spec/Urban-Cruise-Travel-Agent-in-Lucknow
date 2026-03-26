from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Destination(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='destinations/')
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}, {self.country}"

    class Meta:
        verbose_name_plural = "Destinations"


class Tour(models.Model):
    TOUR_TYPES = [
        ('adventure', 'Adventure'),
        ('cultural', 'Cultural'),
        ('relaxation', 'Relaxation'),
        ('urban', 'Urban Exploration'),
        ('nature', 'Nature'),
    ]

    DURATION_CHOICES = [
        (1, '1 Day'),
        (2, '2 Days'),
        (3, '3 Days'),
        (7, '1 Week'),
        (14, '2 Weeks'),
        (21, '3 Weeks'),
    ]

    title = models.CharField(max_length=200)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='tours')
    description = models.TextField()
    tour_type = models.CharField(max_length=20, choices=TOUR_TYPES)
    duration = models.IntegerField(choices=DURATION_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    max_travelers = models.IntegerField()
    image = models.ImageField(upload_to='tours/')
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def available_spots(self):
        booked = self.bookings.filter(status='confirmed').count()
        return self.max_travelers - booked


class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='bookings')
    travelers_count = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    booking_date = models.DateTimeField(auto_now_add=True)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    special_requests = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.tour.title}"

    def save(self, *args, **kwargs):
        self.total_price = self.tour.price * self.travelers_count
        super().save(*args, **kwargs)


class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.tour.title} - {self.rating} stars"

    class Meta:
        unique_together = ['user', 'tour']


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
