

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Set seed for reproducibility
random.seed(42)
np.random.seed(42)

def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

def random_time():
    return (datetime.min + timedelta(minutes=random.randint(600, 1320))).time()

start_date = datetime(2022, 1, 1)
end_date = datetime(2023, 12, 31)

cities = ["Mumbai", "Delhi", "Bengaluru", "Hyderabad", "Pune", "Chennai", "Kolkata"]
restaurant_names = [
    "Barbeque Nation", "Biryani Blues", "The Great Kabab Factory", "Paradise Biryani", "Domino's Pizza",
    "Burger King", "Behrouz Biryani", "Oven Story Pizza", "Faasos", "Sweet Truth", "Subway", "Pizza Hut",
    "McDonald's", "KFC", "Cafe Coffee Day", "Starbucks", "Chai Point", "Wow! Momo", "FreshMenu", "LunchBox"
]

# Generate Restaurants
restaurants = pd.DataFrame([{
    "restaurant_id": i,
    "restaurant_name": random.choice(restaurant_names) + f" #{i}",
    "city": random.choice(cities),
    "opening_hours": "10:00 AM - 11:00 PM"
} for i in range(1, 201)])

restaurants.to_csv("restaurants1.csv", index=False)
from google.colab import files
files.download('restaurants1.csv')

restaurants
