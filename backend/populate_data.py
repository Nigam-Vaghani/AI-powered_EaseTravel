"""
Script to populate the database with sample destination data.
Run this with: python manage.py shell < populate_data.py
"""

from destinations.models import Destination

# Sample destinations data
destinations_data = [
    {
        'name': 'Paris',
        'country': 'France',
        'description': 'The City of Light, famous for its art, fashion, gastronomy, and culture. Visit the Eiffel Tower, Louvre Museum, Notre-Dame Cathedral, and enjoy French cuisine at charming cafes.',
        'avg_budget': 150000,
        'best_season': 'Spring'
    },
    {
        'name': 'Tokyo',
        'country': 'Japan',
        'description': 'A vibrant metropolis blending ultra-modern with traditional. Experience bustling shopping districts, historic temples, delicious sushi, and cherry blossoms in spring.',
        'avg_budget': 180000,
        'best_season': 'Spring'
    },
    {
        'name': 'Goa',
        'country': 'India',
        'description': 'India\'s beach paradise with Portuguese heritage. Beautiful beaches, water sports, nightlife, historic churches, and fresh seafood. Perfect for both relaxation and adventure.',
        'avg_budget': 40000,
        'best_season': 'Winter'
    },
    {
        'name': 'Dubai',
        'country': 'UAE',
        'description': 'A futuristic city in the desert. Visit the Burj Khalifa, luxurious malls, man-made islands, desert safaris, and experience world-class hospitality.',
        'avg_budget': 100000,
        'best_season': 'Winter'
    },
    {
        'name': 'Bali',
        'country': 'Indonesia',
        'description': 'The Island of Gods, known for its forested volcanic mountains, iconic rice paddies, beaches, and coral reefs. Rich culture, ancient temples, and yoga retreats.',
        'avg_budget': 70000,
        'best_season': 'Summer'
    },
    {
        'name': 'New York',
        'country': 'USA',
        'description': 'The city that never sleeps. Iconic landmarks like Statue of Liberty, Times Square, Central Park, Broadway shows, world-class museums, and diverse cuisine.',
        'avg_budget': 200000,
        'best_season': 'Autumn'
    },
    {
        'name': 'Kerala',
        'country': 'India',
        'description': 'God\'s Own Country with serene backwaters, lush green landscapes, Ayurvedic treatments, wildlife sanctuaries, and beautiful beaches. Experience houseboat cruises and spice plantations.',
        'avg_budget': 50000,
        'best_season': 'Winter'
    },
    {
        'name': 'Singapore',
        'country': 'Singapore',
        'description': 'A modern city-state with stunning architecture, Gardens by the Bay, Marina Bay Sands, diverse food scene, shopping, and efficient public transport.',
        'avg_budget': 120000,
        'best_season': 'Year-round'
    },
    {
        'name': 'Maldives',
        'country': 'Maldives',
        'description': 'Tropical paradise with crystal-clear waters, white sandy beaches, luxury resorts, underwater restaurants, and world-class diving and snorkeling.',
        'avg_budget': 250000,
        'best_season': 'Winter'
    },
    {
        'name': 'Jaipur',
        'country': 'India',
        'description': 'The Pink City of India, rich in history and culture. Visit magnificent forts and palaces like Amber Fort, City Palace, Hawa Mahal, and experience authentic Rajasthani cuisine.',
        'avg_budget': 35000,
        'best_season': 'Winter'
    }
]

# Create destinations
print("Adding sample destinations to the database...")
created_count = 0

for dest_data in destinations_data:
    destination, created = Destination.objects.get_or_create(
        name=dest_data['name'],
        country=dest_data['country'],
        defaults={
            'description': dest_data['description'],
            'avg_budget': dest_data['avg_budget'],
            'best_season': dest_data['best_season']
        }
    )
    if created:
        created_count += 1
        print(f"✓ Created: {destination.name}, {destination.country}")
    else:
        print(f"- Already exists: {destination.name}, {destination.country}")

print(f"\nTotal destinations in database: {Destination.objects.count()}")
print(f"Newly created: {created_count}")
print("\nSample data population complete!")
