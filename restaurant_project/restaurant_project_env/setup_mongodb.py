# setup_mongodb.py

from pymongo import MongoClient

def main():
    # connect to local MongoDB server
    client = MongoClient("mongodb://localhost:27017/")

    # access (or create) a database
    db = client["restaurant_db"]

    # access (or create) the collection
    restaurants = db["restaurants"]

    # example insert
    initial_data = [
        {"name": "Pizza Palace", "street": "Main Street 1", "borough": "Manhattan", "cuisine": "Italian", "grade": "A"},
        {"name": "Sushi Place",  "street": "Second Street 5", "borough": "Queens",    "cuisine": "Japanese","grade": "B"},
    ]
    restaurants.insert_many(initial_data)
    print("Inserted", restaurants.count_documents({}), "documents.")

if __name__ == "__main__":
    main()
