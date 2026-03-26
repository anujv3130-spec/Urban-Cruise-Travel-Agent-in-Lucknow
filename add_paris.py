import os
import django
from django.core.files.uploadedfile import SimpleUploadedFile
import requests
from io import BytesIO

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'urban_cruise.settings')
django.setup()

from travel.models import Destination, Tour, Testimonial

def download_image(url, filename):
    """Download image from URL and return as SimpleUploadedFile"""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return SimpleUploadedFile(
            filename,
            response.content,
            content_type='image/jpeg'
        )
    except:
        return None

def create_paris_destination():
    """Create Paris destination"""
    # Check if Paris already exists
    if Destination.objects.filter(name='Paris').exists():
        print("Paris already exists, skipping...")
        return None
    
    paris_data = {
        'name': 'Paris',
        'country': 'France',
        'description': 'The City of Light, famous for the Eiffel Tower, Louvre Museum, Notre-Dame Cathedral, and romantic atmosphere. Experience world-class art, cuisine, and culture in this iconic European capital.',
        'featured': True,
        'image_url': 'https://images.unsplash.com/photo-1502602898536-47ad22581b52?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80'
    }
    
    image = download_image(paris_data['image_url'], "paris_eiffel_tower.jpg")
    
    paris = Destination.objects.create(
        name=paris_data['name'],
        country=paris_data['country'],
        description=paris_data['description'],
        featured=paris_data['featured'],
        image=image if image else None
    )
    
    print(f"Created destination: {paris.name}")
    return paris

def create_paris_tours(paris):
    """Create tours for Paris"""
    if not paris:
        return
    
    tours_data = [
        {
            'title': 'Paris City Highlights Tour',
            'description': 'Complete Paris experience including Eiffel Tower, Louvre Museum, Notre-Dame Cathedral, Arc de Triomphe, and Seine River cruise. Includes skip-the-line tickets and expert guide.',
            'tour_type': 'urban',
            'duration': 1,
            'price': 149.99,
            'max_travelers': 25,
            'featured': True,
            'image_url': 'https://images.unsplash.com/photo-1502602898536-47ad22581b52?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80'
        },
        {
            'title': 'Romantic Paris Experience',
            'description': 'Perfect for couples! Includes dinner cruise on Seine River, visit to Montmartre, sunset at Eiffel Tower, and romantic walk along Champs-Élysées.',
            'tour_type': 'relaxation',
            'duration': 2,
            'price': 399.99,
            'max_travelers': 15,
            'featured': True,
            'image_url': 'https://images.unsplash.com/photo-1511739001486-6bfe10ce785f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80'
        },
        {
            'title': 'Paris Art & Culture Tour',
            'description': 'Deep dive into Parisian culture with visits to Louvre, Musée d\'Orsay, Versailles Palace, and artist workshops. Includes art historian guide.',
            'tour_type': 'cultural',
            'duration': 3,
            'price': 299.99,
            'max_travelers': 18,
            'featured': False,
            'image_url': 'https://images.unsplash.com/photo-1569880153117-8845c04c7278?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80'
        },
        {
            'title': 'Paris Food & Wine Experience',
            'description': 'Culinary journey through Paris including cooking class, wine tasting, market tours, and visits to famous patisseries and bistros.',
            'tour_type': 'cultural',
            'duration': 2,
            'price': 249.99,
            'max_travelers': 12,
            'featured': False,
            'image_url': 'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80'
        },
        {
            'title': 'Disneyland Paris Adventure',
            'description': 'Family fun at Disneyland Paris with park hopper tickets, character meet-and-greets, fireworks show, and transportation from city center.',
            'tour_type': 'adventure',
            'duration': 1,
            'price': 189.99,
            'max_travelers': 30,
            'featured': True,
            'image_url': 'https://images.unsplash.com/photo-1596424989012-47e3e9f7d3d5?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80'
        }
    ]
    
    for tour_data in tours_data:
        image = download_image(tour_data['image_url'], f"{tour_data['title'].lower().replace(' ', '_')}.jpg")
        
        tour = Tour.objects.create(
            title=tour_data['title'],
            destination=paris,
            description=tour_data['description'],
            tour_type=tour_data['tour_type'],
            duration=tour_data['duration'],
            price=tour_data['price'],
            max_travelers=tour_data['max_travelers'],
            featured=tour_data['featured'],
            image=image if image else None
        )
        print(f"Created tour: {tour.title}")

def create_paris_testimonials():
    """Create testimonials for Paris"""
    testimonials_data = [
        {
            'name': 'Marie Dubois',
            'email': 'marie.dubois@email.com',
            'message': 'The Paris City Highlights Tour was amazing! Our guide was so knowledgeable and we skipped all the long lines. The Eiffel Tower at sunset was magical!',
            'featured': True
        },
        {
            'name': 'John Smith',
            'email': 'john.smith@email.com',
            'message': 'Romantic Paris tour exceeded all expectations! The dinner cruise on Seine was the highlight of our anniversary trip. Merci beaucoup URBAN CRUISE!',
            'featured': True
        },
        {
            'name': 'Sophie Martin',
            'email': 'sophie.martin@email.com',
            'message': 'The Art & Culture tour was perfect for art lovers like me. Visiting Versailles with an expert guide was unforgettable. Highly recommend!',
            'featured': False
        },
        {
            'name': 'Robert Johnson',
            'email': 'robert.johnson@email.com',
            'message': 'Disneyland Paris tour was great for our family! Kids loved the character meetings and the fireworks show was spectacular. Well organized tour!',
            'featured': True
        }
    ]
    
    for testimonial_data in testimonials_data:
        testimonial = Testimonial.objects.create(
            name=testimonial_data['name'],
            email=testimonial_data['email'],
            message=testimonial_data['message'],
            featured=testimonial_data['featured']
        )
        print(f"Created testimonial: {testimonial.name}")

def main():
    print("Adding Paris destination and tours...")
    
    # Create Paris destination
    paris = create_paris_destination()
    
    # Create Paris tours
    create_paris_tours(paris)
    
    # Create Paris testimonials
    create_paris_testimonials()
    
    print("\nParis data loading completed successfully!")
    print(f"Total destinations: {Destination.objects.count()}")
    print(f"Total tours: {Tour.objects.count()}")
    print(f"Total testimonials: {Testimonial.objects.count()}")
    
    # Show destination breakdown by country
    print("\nDestinations by country:")
    destinations_by_country = {}
    for dest in Destination.objects.all():
        if dest.country not in destinations_by_country:
            destinations_by_country[dest.country] = []
        destinations_by_country[dest.country].append(dest.name)
    
    for country, dests in destinations_by_country.items():
        print(f"  {country}: {len(dests)} destinations - {', '.join(dests[:3])}{'...' if len(dests) > 3 else ''}")

if __name__ == '__main__':
    main()
