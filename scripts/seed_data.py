import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import django
from datetime import date, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from django.contrib.auth.models import User
from app1.models import Event

def seed():
    # 1. Create admin user if not exists
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123', first_name='System', last_name='Admin')
        print("Superuser 'admin' created with password 'admin123'.")
    else:
        print("Superuser 'admin' already exists.")

    # 2. Add some events
    today = date.today()
    
    events_data = [
        {
            "title": "Global Tech Summit 2026",
            "date": today + timedelta(days=15),
            "location": "San Francisco, CA",
            "description": "Learn about the latest innovations in AI, Web3, and Cloud computing from world-class industry leaders.",
            "seats": 100,
            "event_type": "Tech",
            "price": 49.99
        },
        {
            "title": "Jazz & Blues Festival",
            "date": today + timedelta(days=30),
            "location": "New Orleans, LA",
            "description": "An evening of smooth jazz and soulful blues with performances by international artists.",
            "seats": 150,
            "event_type": "Concert",
            "price": 25.00
        },
        {
            "title": "React & Next.js Web Workshop",
            "date": today + timedelta(days=5),
            "location": "Online (Virtual)",
            "description": "Hands-on coding workshop teaching modern frontend development using React, Next.js, and Tailwind CSS.",
            "seats": 50,
            "event_type": "Workshop",
            "price": 15.00
        },
        {
            "title": "International Business Conference",
            "date": today + timedelta(days=45),
            "location": "New York, NY",
            "description": "Connect with top global business experts, discover market trends, and networking opportunities.",
            "seats": 80,
            "event_type": "Conference",
            "price": 99.99
        }
    ]

    for item in events_data:
        event, created = Event.objects.get_or_create(
            title=item["title"],
            defaults={
                "date": item["date"],
                "location": item["location"],
                "description": item["description"],
                "seats": item["seats"],
                "event_type": item["event_type"],
                "price": item["price"]
            }
        )
        if created:
            print(f"Event '{event.title}' created successfully.")
        else:
            print(f"Event '{event.title}' already exists.")

if __name__ == "__main__":
    seed()
