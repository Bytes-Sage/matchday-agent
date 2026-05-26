"""
Seed script for MatchDay Agent — World Cup 2026 database.
Populates MongoDB Atlas with all World Cup data.

Usage: python -m data.seed
"""
import os
import sys
import certifi
from pymongo import MongoClient, GEOSPHERE
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("MONGODB_DATABASE", "worldcup2026")

if not MONGODB_URI:
    print("❌ ERROR: MONGODB_URI environment variable is not set.")
    print("   Create a .env file with: MONGODB_URI=mongodb+srv://...")
    sys.exit(1)

# Import all data modules
from data.venues import VENUES_DATA
from data.cities import CITIES_DATA
from data.matches import MATCHES_DATA
from data.restaurants import RESTAURANTS_DATA
from data.extras import FAN_ZONES_DATA, TRANSPORT_DATA


def seed_db():
    print(f"🔗 Connecting to MongoDB Atlas...")
    print(f"   Database: {DB_NAME}")
    
    try:
        client = MongoClient(MONGODB_URI, tlsCAFile=certifi.where())
        # Test connection
        client.admin.command('ping')
        print("✅ Connected successfully!\n")
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        sys.exit(1)
    
    db = client[DB_NAME]
    
    collections = {
        "venues": VENUES_DATA,
        "cities": CITIES_DATA,
        "matches": MATCHES_DATA,
        "restaurants": RESTAURANTS_DATA,
        "fan_zones": FAN_ZONES_DATA,
        "transport": TRANSPORT_DATA,
    }
    
    total_docs = 0
    
    for coll_name, data in collections.items():
        # Drop existing data (idempotent)
        db[coll_name].drop()
        
        # Insert documents
        result = db[coll_name].insert_many(data)
        count = len(result.inserted_ids)
        total_docs += count
        print(f"  📦 {coll_name:15s} → {count:3d} documents inserted")
        
        # Create geospatial indexes where applicable
        if data and isinstance(data[0], dict) and "location" in data[0]:
            db[coll_name].create_index([("location", GEOSPHERE)])
            print(f"  📍 {coll_name:15s} → 2dsphere index created on 'location'")
    
    # Create additional useful indexes
    db.matches.create_index("venueId")
    db.matches.create_index("city")
    db.matches.create_index("stage")
    db.matches.create_index("homeTeam")
    db.matches.create_index("awayTeam")
    db.matches.create_index("date")
    db.restaurants.create_index("venueId")
    print(f"\n  🔑 Additional indexes created on matches and restaurants")
    
    print(f"\n{'='*50}")
    print(f"✅ Seeding complete!")
    print(f"   Total documents: {total_docs}")
    print(f"   Collections: {len(collections)}")
    print(f"{'='*50}")
    print(f"\n⚠️  NEXT STEP: Create the Vector Search index in Atlas UI")
    print(f"   Go to: Atlas → Search & Vector Search → Create Index")
    print(f"   Collection: worldcup2026.matches")
    print(f"   Field: 'embedding' (768 dimensions, cosine)")
    
    client.close()


if __name__ == "__main__":
    seed_db()
