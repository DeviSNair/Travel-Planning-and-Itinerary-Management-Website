import math
import urllib.parse
from pymongo import MongoClient

# 1. Database Connection Setup
password = urllib.parse.quote_plus("Devi@2003")
uri = f"mongodb+srv://devisumanair_db_user:{password}@surveydata.9ohe7ek.mongodb.net/?appName=SurveyData"
client = MongoClient(uri)
db = client["Trivandrum_Travel_Database"]
collection = db["locations"]

def calculate_distance(lat1, lon1, lat2, lon2):
    """Haversine formula to calculate distance in km."""
    R = 6371  # Earth radius
    d_lat = math.radians(lat2 - lat1)
    d_lon = math.radians(lon2 - lon1)
    a = (math.sin(d_lat / 2)**2 + 
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(d_lon / 2)**2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def get_optimized_route(start_coords, selected_names):
    """Greedy Algorithm to find the next closest location."""
    # Fetch selected locations from MongoDB
    targets = list(collection.find({"Name": {"$in": selected_names}}))
    
    route = []
    current_lat, current_lon = start_coords
    
    while targets:
        # Find the closest location from the remaining targets
        closest_node = min(
            targets, 
            key=lambda x: calculate_distance(current_lat, current_lon, x['Latitude'], x['Longitude'])
        )
        
        # Calculate distance to that node for the log
        dist = calculate_distance(current_lat, current_lon, closest_node['Latitude'], closest_node['Longitude'])
        
        route.append({
            "Name": closest_node['Name'],
            "Distance_From_Last_Stop": round(dist, 2)
        })
        
        # Move to the new location
        current_lat = closest_node['Latitude']
        current_lon = closest_node['Longitude']
        targets.remove(closest_node)
        
    return route

# --- TEST THE LOGIC ---
if __name__ == "__main__":
    # Example: User is at TVM Central Railway Station
    my_location = (8.4818, 76.9515) 
    
    # Example: User wants to visit these 4 specific spots
    user_picks = [
        "Lulu Mall Trivandrum", 
        "Kovalam Lighthouse Beach", 
        "Napier Museum", 
        "Azhimala Shiva Statue"
    ]
    
    print("\n📍 Starting Point: Trivandrum Central")
    print("🔄 Calculating Optimized Dora Map Route...\n")
    
    optimized_path = get_optimized_route(my_location, user_picks)
    
    for i, stop in enumerate(optimized_path, 1):
        print(f"Step {i}: Go to {stop['Name']} ({stop['Distance_From_Last_Stop']} km away)")

    print("\n✅ Route Optimization Complete!")