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

def create_more_indian_destinations():
    """Create more famous Indian destinations"""
    destinations_data = [
        {
            'name': 'Golden Temple',
            'country': 'India',
            'description': 'The holiest shrine of Sikhism in Amritsar, Punjab. Known for its stunning golden architecture and spiritual atmosphere.',
            'featured': True,
            'image_url': 'https://images.unsplash.com/photo-1589391886645-d51941baf7fb?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80'
        },
        {
            'name': 'Goa Beaches',
            'country': 'India',
            'description': 'Famous beach destination with pristine beaches, Portuguese architecture, and vibrant nightlife. Perfect for relaxation and water sports.',
            'featured': True,
            'image_url': 'https://images.unsplash.com/photo-1512343879784-a960bf40e7f1?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80'
        },
        {
            'name': 'Mysore Palace',
            'country': 'India',
            'description': 'Magnificent royal palace in Mysore, Karnataka. Known for its stunning architecture and the famous Dussehra celebrations.',
            'featured': True,
            'image_url': 'https://images.unsplash.com/photo-1593696140826-c58b021acf8b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80'
        },
        {
            'name': 'Hampi',
            'country': 'India',
            'description': 'UNESCO World Heritage Site featuring ancient temple ruins of the Vijayanagara Empire. A paradise for history lovers.',
            'featured': False,
            'image_url': 'https://images.unsplash.com/photo-1593696140826-c58b021acf8b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80'
        },
        {
            'name': 'Rishikesh',
            'country': 'India',
            'description': 'Yoga capital of the world located on the banks of the Ganges. Known for spirituality, adventure sports, and ashrams.',
            'featured': True,
            'image_url': 'https://images.unsplash.com/photo-1544735716-392fe2489ffa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80'
        },
        {
            'name': 'Khajuraho Temples',
            'country': 'India',
            'description': 'Group of Hindu and Jain temples famous for their intricate sculptures and architectural excellence. UNESCO World Heritage Site.',
            'featured': False,
            'image_url': 'https://images.unsplash.com/photo-1524492412937-b28074a5d7da?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80'
        },
        {
            'name': 'Ladakh',
            'country': 'India',
            'description': 'High-altitude desert region in the Himalayas known for breathtaking landscapes, Buddhist monasteries, and adventure tourism.',
            'featured': True,
            'image_url': 'https://images.unsplash.com/photo-1544735716-392fe2489ffa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80'
        },
        {
            'name': 'Sundarbans',
            'country': 'India',
            'description': 'World\'s largest mangrove forest and UNESCO World Heritage Site. Home to the Royal Bengal Tiger and unique ecosystem.',
            'featured': False,
            'image_url': 'https://images.unsplash.com/photo-1528722828814-77b9b83aafb2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80'
        }
    ]
    
    created_destinations = []
    for dest_data in destinations_data:
        # Check if destination already exists
        if Destination.objects.filter(name=dest_data['name']).exists():
            print(f"Destination {dest_data['name']} already exists, skipping...")
            continue
            
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

def create_more_tours(destinations):
    """Create tours for new Indian destinations"""
    tours_data = [
        {
            'title': 'Golden Temple Spiritual Tour',
            'destination': destinations[0] if len(destinations) > 0 else None,
            'description': 'Experience the divine atmosphere of the Golden Temple with community kitchen visit, evening ceremony, and local Punjabi cuisine.',
            'tour_type': 'cultural',
            'duration': 2,
            'price': 99.99,
            'max_travelers': 20,
            'featured': True,
            'image_url': 'https://images.unsplash.com/photo-1589391886645-d51941baf7fb?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80'
        },
        {
            'title': 'Goa Beach Paradise',
            'destination': destinations[1] if len(destinations) > 1 else None,
            'description': 'Perfect beach getaway with water sports, beach hopping, Portuguese heritage tour, and vibrant nightlife experience.',
            'tour_type': 'relaxation',
            'duration': 3,
            'price': 179.99,
            'max_travelers': 25,
            'featured': True,
            'image_url': 'https://images.unsplash.com/photo-1512343879784-a960bf40e7f1?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80'
        },
        {
            'title': 'Mysore Royal Heritage',
            'destination': destinations[2] if len(destinations) > 2 else None,
            'description': 'Explore the grand Mysore Palace, Chamundi Hills, and experience the royal lifestyle with traditional South Indian cultural show.',
            'tour_type': 'cultural',
            'duration': 2,
            'price': 119.99,
            'max_travelers': 18,
            'featured': False,
            'image_url': 'https://images.unsplash.com/photo-1593696140826-c58b021acf8b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80'
        },
        {
            'title': 'Hampi Heritage Expedition',
            'destination': destinations[3] if len(destinations) > 3 else None,
            'description': 'Explore the ancient ruins of Hampi with expert guide, sunrise at Virupaksha Temple, and coracle ride on Tungabhadra River.',
            'tour_type': 'adventure',
            'duration': 3,
            'price': 159.99,
            'max_travelers': 15,
            'featured': False,
            'image_url': 'https://images.unsplash.com/photo-1593696140826-c58b021acf8b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80'
        },
        {
            'title': 'Rishikesh Yoga & Adventure',
            'destination': destinations[4] if len(destinations) > 4 else None,
            'description': 'Combine yoga sessions, meditation, Ganga Aarti, and adventure sports like river rafting and bungee jumping.',
            'tour_type': 'adventure',
            'duration': 4,
            'price': 219.99,
            'max_travelers': 20,
            'featured': True,
            'image_url': 'https://images.unsplash.com/photo-1544735716-392fe2489ffa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80'
        },
        {
            'title': 'Ladakh Himalayan Adventure',
            'destination': destinations[6] if len(destinations) > 6 else None,
            'description': 'Ultimate Himalayan experience with monastery visits, Pangong Lake, Nubra Valley, and high-altitude trekking.',
            'tour_type': 'adventure',
            'duration': 7,
            'price': 599.99,
            'max_travelers': 12,
            'featured': True,
            'image_url': 'https://images.unsplash.com/photo-1544735716-392fe2489ffa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80'
        }
    ]
    
    for tour_data in tours_data:
        if tour_data['destination'] is None:
            continue
            
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

def create_more_testimonials():
    """Create additional testimonials"""
    testimonials_data = [
        {
            'name': 'Amit Kumar',
            'email': 'amit.kumar@email.com',
            'message': 'The Ladakh trip was life-changing! The Himalayan views were breathtaking and the monasteries were so peaceful. Thank you URBAN CRUISE!',
            'featured': True
        },
        {
            'name': 'Sneha Gupta',
            'email': 'sneha.gupta@email.com',
            'message': 'Goa beach tour was perfect! The beaches were clean, water sports were thrilling, and the nightlife was amazing. Best vacation ever!',
            'featured': True
        },
        {
            'name': 'Vikram Singh',
            'email': 'vikram.singh@email.com',
            'message': 'Golden Temple visit was spiritually uplifting. The langar experience and evening ceremony were unforgettable. Highly recommend!',
            'featured': False
        },
        {
            'name': 'Neha Patel',
            'email': 'neha.patel@email.com',
            'message': 'Rishikesh yoga retreat helped me find inner peace. The combination of yoga, meditation, and adventure sports was perfect.',
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
    print("Loading more Indian destinations and tours data...")
    
    # Create more destinations
    destinations = create_more_indian_destinations()
    
    # Create more tours
    if destinations:
        create_more_tours(destinations)
    
    # Create more testimonials
    create_more_testimonials()
    
    print("\nAdditional data loading completed successfully!")
    print(f"Total destinations: {Destination.objects.count()}")
    print(f"Total tours: {Tour.objects.count()}")
    print(f"Total testimonials: {Testimonial.objects.count()}")

if __name__ == '__main__':
    main()
