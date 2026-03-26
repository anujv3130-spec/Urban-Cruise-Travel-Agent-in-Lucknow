from django.core.management.base import BaseCommand
from travel.models import Destination, Tour, Testimonial
from django.core.files import File
import requests
from io import BytesIO
import os

class Command(BaseCommand):
    help = 'Add Vindhyachal destination with tours and testimonials'

    def handle(self, *args, **options):
        # Create Vindhyachal destination
        destination = Destination.objects.create(
            name='Vindhyachal',
            country='India',
            state='Uttar Pradesh',
            city='Lucknow',
            description='Vindhyachal is a sacred city located on banks of the Ganges River, known for the Vindhyavasini Devi Temple. This spiritual destination attracts pilgrims from across India and offers a blend of religious significance and natural beauty.',
            featured=True
        )
        
        # Add tours
        tours_data = [
            {
                'title': 'Vindhyachal Pilgrimage Tour',
                'description': 'Complete spiritual journey to Vindhyachal with temple visits and Ganga Aarti experience.',
                'duration': 2,
                'price': 2999,
                'tour_type': 'cultural',
                'max_travelers': 20,
                'featured': True
            },
            {
                'title': 'Lucknow-Vindhyachal Heritage Tour',
                'description': 'Explore the cultural heritage of Lucknow and spiritual significance of Vindhyachal in one comprehensive tour.',
                'duration': 3,
                'price': 4999,
                'tour_type': 'cultural',
                'max_travelers': 15,
                'featured': False
            }
        ]
        
        for tour_data in tours_data:
            Tour.objects.create(
                destination=destination,
                **tour_data
            )
        
        # Add testimonials
        testimonials_data = [
            {
                'name': 'Priya Sharma',
                'message': 'The Vindhyachal pilgrimage tour was spiritually uplifting. Well organized and peaceful experience.',
                'rating': 5
            },
            {
                'name': 'Rajesh Kumar',
                'message': 'Great combination of Lucknow heritage and Vindhyachal spirituality. Highly recommend!',
                'rating': 4
            }
        ]
        
        for testimonial_data in testimonials_data:
            Testimonial.objects.create(
                **testimonial_data
            )
        
        self.stdout.write(self.style.SUCCESS('Vindhyachal destination added successfully!'))
