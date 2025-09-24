# setup_mongodb.py

from pymongo import MongoClient

# Step 1: Connect to MongoDB server
client = MongoClient('mongodb://localhost:27017/')

# Step 2: Create or access the database
db = client['restaurant_db']

# Step 3: Create or access the collection
restaurants_collection = db['restaurants']

# Step 4: Insert initial data
initial_data = [
    {
        "name": "Pizza Palace",
        "street": "Main Street 1",
        "borough": "Manhattan",
        "cuisine": "Italian",
        "grade": "A"
    },
    {
        "name": "Sushi Place",
        "street": "Second Street 5",
        "borough": "Queens",
        "cuisine": "Japanese",
        "grade": "B"
    },
    {
        "name": "Burger Spot",
        "street": "Third Avenue 77",
        "borough": "Bronx",
        "cuisine": "American",
        "grade": "A"
    },
    {
        "name": "Curry House",
        "street": "Fourth Blvd 88",
        "borough": "Brooklyn",
        "cuisine": "Indian",
        "grade": "A"
    },
    {
        "name": "Taco Town",
        "street": "Fifth Road 99",
        "borough": "Staten Island",
        "cuisine": "Mexican",
        "grade": "C"
    }
]

# Step 5: Insert data if collection is empty
if restaurants_collection.count_documents({}) == 0:
    restaurants_collection.insert_many(initial_data)
    print("Initial restaurant data inserted successfully.")
else:
    print("Restaurant collection already has data.")

# Done!
