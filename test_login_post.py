#!/usr/bin/env python
import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'urban_cruise.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User

# Create a test client
client = Client()

# Test login POST request
try:
    # Get the login page first (to get CSRF token)
    response = client.get('/accounts/login/')
    print(f"✅ Login page status: {response.status_code}")
    
    # Test login with POST
    response = client.post('/accounts/login/', {
        'username': 'user',
        'password': '47738'
    })
    
    print(f"✅ Login POST status: {response.status_code}")
    
    # Check if user is authenticated
    if response.status_code == 302:  # Redirect after successful login
        print("✅ Login successful - redirect detected")
        print(f"✅ Redirect location: {response.get('Location', 'No location')}")
    else:
        print(f"❌ Login failed - status code: {response.status_code}")
        if response.status_code == 200:
            print("❌ Form errors may be present")
            
except Exception as e:
    print(f"❌ Error: {e}")
