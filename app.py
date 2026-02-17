from flask import Flask, request, jsonify
from flask_cors import CORS
import math
import urllib.parse
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)  # This allows your teammate's frontend to talk to your backend!

# 1. MongoDB Setup
password = urllib.parse.quote_plus("Devi@2003")
uri = f"mongodb+srv://devisumanair_db_user:{password}@surveydata.9ohe7ek.mongodb.net/?appName=SurveyData"
client = MongoClient(uri)
db = client["Trivandrum_Travel_Database"]
collection = db["locations"]

def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371
    d_lat = math.radians(lat2 - lat1)
    d_lon = math.radians(lon2 - lon1)
    a = (math.sin(d_lat / 2)**2 + 
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(d_lon / 2)**2)
    return R * (2 * math.atan2(math.sqrt(a), math.sqrt(1 - a)))

# 2. The API Endpoint
@app.route('/get_route', methods=['POST'])
def get_route():
    data = request.json
    # Expecting: {"start": [lat, lon], "selected": ["Place1", "Place2"]}
    start_coords = data.get('start')
    selected_names = data.get('selected')

    # Fetch locations from DB
    targets = list(collection.find({"Name": {"$in": selected_names}}))
    
    route = []
    current_lat, current_lon = start_coords[0], start_coords[1]
    
    while targets:
        closest_node = min(
            targets, 
            key=lambda x: calculate_distance(current_lat, current_lon, x['Latitude'], x['Longitude'])
        )
        
        dist = calculate_distance(current_lat, current_lon, closest_node['Latitude'], closest_node['Longitude'])
        
        route.append({
            "name": closest_node['Name'],
            "lat": closest_node['Latitude'],
            "lon": closest_node['Longitude'],
            "dist": round(dist, 2)
        })
        
        current_lat, current_lon = closest_node['Latitude'], closest_node['Longitude']
        targets.remove(closest_node)
        
    return jsonify({"status": "success", "route": route})

if __name__ == "__main__":
    print("🚀 Dora Map Backend is running on http://127.0.0.1:5000")
    app.run(debug=True)