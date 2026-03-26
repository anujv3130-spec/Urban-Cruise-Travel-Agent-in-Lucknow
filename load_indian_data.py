import os
import django
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management.base import BaseCommand
from django.conf import settings
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

def create_indian_destinations():
    """Create famous Indian destinations"""
    destinations_data = [
        {
            'name': 'Taj Mahal',
            'country': 'India',
            'description': 'The iconic white marble mausoleum in Agra, one of the Seven Wonders of the World. Built by Mughal Emperor Shah Jahan in memory of his wife Mumtaz Mahal.',
            'featured': True,
            'image_url': 'https://images.unsplash.com/photo-1524492412937-b28074a5d7da?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80'
        },
        {
            'name': 'Red Fort',
            'country': 'India',
            'description': 'Historic fort in Delhi that served as the main residence of the Mughal emperors for nearly 200 years. A UNESCO World Heritage Site.',
            'featured': True,
            'image_url': 'https://images.unsplash.com/photo-1593696140826-c58b021acf8b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80'
        },
        {
            'name': 'Gateway of India',
            'country': 'India',
            'description': 'Iconic monument and arch in Mumbai, built during the British Raj. Located on the waterfront in the Apollo Bunder area.',
            'featured': True,
            'image_url': 'https://images.unsplash.com/photo-1589391886645-d51941baf7fb?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80'
        },
        {
            'name': 'Jaipur - Pink City',
            'country': 'India',
            'description': 'The capital of Rajasthan, known for its distinctive pink-colored buildings. Home to magnificent palaces, forts, and vibrant markets.',
            'featured': True,
            'image_url': 'https://images.unsplash.com/photo-1593696140826-c58b021acf8b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80'
        },
        {
            'name': 'Varanasi',
            'country': 'India',
            'description': 'One of the oldest continuously inhabited cities in the world. Sacred to Hindus and known for its ghats along the Ganges River.',
            'featured': False,
            'image_url': 'https://images.unsplash.com/photo-1528722828814-77b9b83aafb2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80'
        },
        {
            'name': 'Kerala Backwaters',
            'country': 'India',
            'description': 'Network of interconnected canals, rivers, lakes, and inlets in Kerala. Famous for houseboat cruises and serene natural beauty.',
            'featured': True,
            'image_url': 'https://images.unsplash.com/photo-1544735716-392fe2489ffa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80'
        }
    ]
    
    created_destinations = []
    for dest_data in destinations_data:
        image = download_image(dest_data['image_url'], f"{dest_data['name'].lower().replace(' ', '_')}.jpg")
        
        destination = Destination.objects.create(
            name=dest_data['name'],
            country=dest_data['country'],
            description=dest_data['description'],
            featured=dest_data['featured'],
            image=image if image else None
        )
        created_destinations.append(destination)
        print(f"Created destination: {destination.name}")
    
    return created_destinations

def create_tours(destinations):
    """Create tours for Indian destinations"""
    tours_data = [
        {
            'title': 'Taj Mahal Sunrise Tour',
            'destination': destinations[0],  # Taj Mahal
            'description': 'Experience the breathtaking beauty of the Taj Mahal at sunrise. Includes guided tour, breakfast, and transportation from Delhi.',
            'tour_type': 'cultural',
            'duration': 1,
            'price': 89.99,
            'max_travelers': 20,
            'featured': True,
            'image_url': 'https://images.unsplash.com/photo-1524492412937-b28074a5d7da?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80'
        },
        {
            'title': 'Delhi Heritage Walk',
            'destination': destinations[1],  # Red Fort
            'description': 'Explore the rich history of Old Delhi including Red Fort, Jama Masjid, and Chandni Chowk. Includes lunch and expert guide.',
            'tour_type': 'cultural',
            'duration': 1,
            'price': 45.99,
            'max_travelers': 15,
            'featured': False,
            'image_url': 'https://images.unsplash.com/photo-1593696140826-c58b021acf8b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80'
        },
        {
            'title': 'Mumbai City Tour',
            'destination': destinations[2],  # Gateway of India
            'description': 'Complete Mumbai experience including Gateway of India, Marine Drive, Elephanta Caves, and local street food tour.',
            'tour_type': 'urban',
            'duration': 2,
            'price': 125.99,
            'max_travelers': 25,
            'featured': True,
            'image_url': 'https://images.unsplash.com/photo-1589391886645-d51941baf7fb?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80'
        },
        {
            'title': 'Rajasthan Royal Experience',
            'destination': destinations[3],  # Jaipur
            'description': 'Luxury tour of the Pink City including Amber Fort, City Palace, and traditional Rajasthani dinner with cultural show.',
            'tour_type': 'cultural',
            'duration': 3,
            'price': 299.99,
            'max_travelers': 12,
            'featured': True,
            'image_url': 'https://images.unsplash.com/photo-1593696140826-c58b021acf8b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80'
        },
        {
            'title': 'Varanasi Spiritual Journey',
            'destination': destinations[4],  # Varanasi
            'description': 'Spiritual experience including Ganga Aarti, temple visits, boat ride on Ganges, and exploration of ancient city lanes.',
            'tour_type': 'cultural',
            'duration': 2,
            'price': 189.99,
            'max_travelers': 18,
            'featured': False,
            'image_url': 'https://images.unsplash.com/photo-1528722828814-77b9b83aafb2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80'
        },
        {
            'title': 'Kerala Houseboat Experience',
            'destination': destinations[5],  # Kerala Backwaters
            'description': 'Overnight stay on traditional Kerala houseboat with all meals, village visits, and sunset cruise in Alleppey backwaters.',
            'tour_type': 'relaxation',
            'duration': 2,
            'price': 249.99,
            'max_travelers': 8,
            'featured': True,
            'image_url': 'https://images.unsplash.com/photo-1544735716-392fe2489ffa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80'
        }
    ]
    
    for tour_data in tours_data:
        image = download_image(tour_data['image_url'], f"{tour_data['title'].lower().replace(' ', '_')}.jpg")
        
        tour = Tour.objects.create(
            title=tour_data['title'],
            destination=tour_data['destination'],
            description=tour_data['description'],
            tour_type=tour_data['tour_type'],
            duration=tour_data['duration'],
            price=tour_data['price'],
            max_travelers=tour_data['max_travelers'],
            featured=tour_data['featured'],
            image=image if image else None
        )
        print(f"Created tour: {tour.title}")

def create_testimonials():
    """Create sample testimonials"""
    testimonials_data = [
        {
            'name': 'Priya Sharma',
            'email': 'priya.sharma@email.com',
            'message': 'The Taj Mahal sunrise tour was absolutely magical! Our guide was knowledgeable and the arrangements were perfect. Highly recommend URBAN CRUISE!',
            'featured': True
        },
        {
            'name': 'Raj Patel',
            'email': 'raj.patel@email.com',
            'message': 'Amazing experience exploring Rajasthan. The palaces and forts were breathtaking. The cultural show and dinner were the highlight of our trip.',
            'featured': True
        },
        {
            'name': 'Anita Reddy',
            'email': 'anita.reddy@email.com',
            'message': 'The Kerala houseboat experience was beyond our expectations. Peaceful, beautiful, and the food was delicious. Will definitely book again!',
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
    print("Loading Indian destinations and tours data...")
    
    # Create destinations
    destinations = create_indian_destinations()
    
    # Create tours
    create_tours(destinations)
    
    # Create testimonials
    create_testimonials()
    
    print("\nData loading completed successfully!")
    print(f"Created {Destination.objects.count()} destinations")
    print(f"Created {Tour.objects.count()} tours")
    print(f"Created {Testimonial.objects.count()} testimonials")

if __name__ == '__main__':
    main()
