#!/usr/bin/env python
import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'urban_cruise.settings')
django.setup()

from django.contrib.auth import authenticate, login
from django.test import RequestFactory
from django.contrib.auth.models import User

# Test user existence
try:
    user = User.objects.get(username='user')
    print(f"✅ User found: {user.username} (ID: {user.id})")
    
    # Test password
    if user.check_password('47738'):
        print("✅ Password is correct")
        
        # Test authentication
        auth_user = authenticate(username='user', password='47738')
        if auth_user:
            print("✅ Authentication successful")
            print(f"✅ Authenticated user: {auth_user.username}")
        else:
            print("❌ Authentication failed")
    else:
        print("❌ Password is incorrect")
        
except User.DoesNotExist:
    print("❌ User does not exist")
except Exception as e:
    print(f"❌ Error: {e}")
