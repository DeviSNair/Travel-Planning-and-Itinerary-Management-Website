# 🗺️ Travel Planning and Itinerary Management - Trivandrum

An intelligent itinerary management system that optimizes travel routes for tourists in Trivandrum using a **Greedy Search Algorithm** and **Cloud Database** integration.

## 🚀 Features
* **Automated Route Optimization:** Uses the Haversine formula to calculate real-world distances.
* **Cloud Integration:** Powered by MongoDB Atlas for real-time data persistence.
* **RESTful API:** A Flask-based backend that serves optimized JSON data to the frontend.
* **Curated Locations:** 28+ top-rated spots in Trivandrum categorized by "Vibe."

## 📊 Data Model
Each location in the MongoDB collection contains:
* `Name`: (String) Official name of the landmark.
* `Category`: (String) Vibe/Type (e.g., Holy Places, Beaches).
* `Coordinates`: (Float) Latitude & Longitude for GPS mapping.
* `Hours/Fee`: (String) Essential tourist metadata.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Backend Framework:** Flask
* **Database:** MongoDB Atlas (NoSQL)
* **Data Handling:** Pandas, Openpyxl
* **Security:** Flask-CORS

## 🧠 The Algorithm (Greedy Search)
The backend solves a variant of the **Traveling Salesman Problem (TSP)**. 
1. **Distance Calculation:** It uses the **Haversine Formula** to calculate the shortest distance over the Earth's surface between two sets of GPS coordinates (Latitude/Longitude).
2. **Pathfinding:** It uses a **Greedy Approach**—starting from the user's current location, the algorithm identifies the closest selected spot, moves there, and repeats the process until the itinerary is complete.

### 🧠 The Math behind the Map
The system calculates distances using the **Haversine Formula** to account for the Earth's curvature, ensuring the "Greedy" choice is geographically accurate:
$$d = 2r \arcsin\left(\sqrt{\sin^2\left(\frac{\Delta\phi}{2}\right) + \cos(\phi_1)\cos(\phi_2)\sin^2\left(\frac{\Delta\lambda}{2}\right)}\right)$$

## 📂 Project Structure
* `app.py`: The main Flask API and server logic.
* `route_optimizer.py`: The core Greedy Algorithm and distance math.
* `upload_to_mongodb.py`: ETL script to refresh cloud data.
* `create_database.py`: Data structuring script.

## ⚙️ Setup & Installation
1. Install dependencies:
   ```bash
   pip install flask flask-cors pymongo pandas openpyxl```

2. Run the Backend:
   ```bash
   python app.py```
   
   The server will start at http://127.0.0.1:5000

📡 API Documentation
Get Optimized Route
Endpoint: /get_route

Method: POST

Payload Format:

```JSON
{
  "start": [8.4818, 76.9515],
  "selected": ["Napier Museum", "Lulu Mall Trivandrum", "Kovalam Beach"]
}
Success Response: A JSON object containing the status and an ordered route list with distances and coordinates.```



Developed as part of the College Mini-Project (2026).
