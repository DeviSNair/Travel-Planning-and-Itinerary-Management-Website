import pandas as pd

# The Master Database: Merged from your Word Doc and PDF Coordinates
full_data = [
    # --- HOLY PLACES (Spiritual Vibe) ---
    {"Name": "Sri Padmanabhaswamy Temple", "Category": "Holy Places", "Latitude": 8.4828, "Longitude": 76.9434, "Hours": "3:30 AM-12:00 PM, 5:00 PM-7:20 PM", "Fee": "Free", "Notes": "Strict dress code (Dhoti)"},
    {"Name": "Attukal Bhagavathy Temple", "Category": "Holy Places", "Latitude": 8.4673, "Longitude": 76.9550, "Hours": "4:30 AM-12:30 PM, 5:00 PM-8:30 PM", "Fee": "Free", "Notes": "Women's Sabarimala"},
    {"Name": "Pazhavangadi Ganapathy Temple", "Category": "Holy Places", "Latitude": 8.4855, "Longitude": 76.9440, "Hours": "4:30 AM-10:45 AM, 5:00 PM-8:00 PM", "Fee": "Free", "Notes": "Managed by Indian Army"},
    {"Name": "Beemapally Dargah Shareef", "Category": "Holy Places", "Latitude": 8.4520, "Longitude": 76.9300, "Hours": "24 Hours", "Fee": "Free", "Notes": "Chandanakkudam festival"},
    {"Name": "St. Joseph’s Cathedral (Palayam)", "Category": "Holy Places", "Latitude": 8.5069, "Longitude": 76.9558, "Hours": "6:00 AM-6:00 PM", "Fee": "Free", "Notes": "Gothic style architecture"},
    {"Name": "Azhimala Shiva Statue", "Category": "Holy Places", "Latitude": 8.3500, "Longitude": 77.0100, "Hours": "5:30 AM-8:00 PM", "Fee": "Free", "Notes": "Largest Shiva statue in Kerala"},
    {"Name": "Karikkakom Chamundi Devi Temple", "Category": "Holy Places", "Latitude": 8.5082, "Longitude": 76.9030, "Hours": "5:00 AM-12:00 PM", "Fee": "Free", "Notes": "Ancient 600-year old temple"},
    {"Name": "Madavoorpara Rock Cut Temple", "Category": "Holy Places", "Latitude": 8.5637, "Longitude": 76.8752, "Hours": "9:00 AM-6:00 PM", "Fee": "Free", "Notes": "8th-century heritage site"},

    # --- BEACHES & NATURE (Relaxing/Scenic Vibe) ---
    {"Name": "Kovalam Lighthouse Beach", "Category": "Beaches", "Latitude": 8.4020, "Longitude": 76.9784, "Hours": "24 Hours", "Fee": "Free", "Notes": "Climb lighthouse for view"},
    {"Name": "Hawa Beach (Kovalam)", "Category": "Beaches", "Latitude": 8.4010, "Longitude": 76.9770, "Hours": "24 Hours", "Fee": "Free", "Notes": "Sunrise/Sunset point"},
    {"Name": "Varkala Cliff & Beach", "Category": "Beaches", "Latitude": 8.7330, "Longitude": 76.7070, "Hours": "24 Hours", "Fee": "Free", "Notes": "Unique sedimentary cliffs"},
    {"Name": "Shangumugham Beach", "Category": "Beaches", "Latitude": 8.4791, "Longitude": 76.9116, "Hours": "24 Hours", "Fee": "Free", "Notes": "Near TVM Airport"},
    {"Name": "Poovar Island & Backwaters", "Category": "Backwaters", "Latitude": 8.3180, "Longitude": 77.0700, "Hours": "9:00 AM-6:00 PM", "Fee": "Boat Hire", "Notes": "Floating restaurants"},
    {"Name": "Veli Tourist Village", "Category": "Nature", "Latitude": 8.5097, "Longitude": 76.8906, "Hours": "9:00 AM-8:00 PM", "Fee": "INR 20", "Notes": "Floating bridge and lake"},
    {"Name": "Akkulam Tourist Village", "Category": "Nature", "Latitude": 8.5200, "Longitude": 76.9050, "Hours": "10:00 AM-8:00 PM", "Fee": "INR 20", "Notes": "Children's park and boating"},

    # --- MUSEUMS, CULTURE & HERITAGE (Educational Vibe) ---
    {"Name": "Napier Museum", "Category": "Museums", "Latitude": 8.5085, "Longitude": 76.9547, "Hours": "10:00 AM-4:45 PM", "Fee": "INR 20", "Notes": "Closed on Mondays"},
    {"Name": "Kuthira Malika (Mansion of Horses)", "Category": "Museums", "Latitude": 8.4836, "Longitude": 76.9455, "Hours": "8:30 AM-1:00 PM, 3:00 PM-5:30 PM", "Fee": "INR 50", "Notes": "Travancore Royal Family"},
    {"Name": "Trivandrum Zoo", "Category": "Nature", "Latitude": 8.5095, "Longitude": 76.9550, "Hours": "9:00 AM-5:15 PM", "Fee": "INR 30", "Notes": "Oldest zoo in India"},
    {"Name": "Priyadarshini Planetarium", "Category": "Education", "Latitude": 8.5042, "Longitude": 76.9472, "Hours": "10:00 AM-5:00 PM", "Fee": "INR 60", "Notes": "Part of Science Tech Museum"},
    {"Name": "Kerala Secretariat", "Category": "Heritage", "Latitude": 8.5061, "Longitude": 76.9560, "Hours": "External View", "Fee": "Free", "Notes": "Administrative heart of Kerala"},
    {"Name": "Kanakakkunnu Palace", "Category": "Heritage", "Latitude": 8.5090, "Longitude": 76.9590, "Hours": "10:00 AM-9:00 PM", "Fee": "Free", "Notes": "Host of cultural festivals"},

    # --- MODERN, SHOPPING & FUN (Lively Vibe) ---
    {"Name": "Lulu Mall Trivandrum", "Category": "Modern", "Latitude": 8.4916, "Longitude": 76.8942, "Hours": "10:00 AM-11:00 PM", "Fee": "Free", "Notes": "Funtura & Hypermarket"},
    {"Name": "Mall of Travancore", "Category": "Modern", "Latitude": 8.4715, "Longitude": 76.9150, "Hours": "10:00 AM-11:00 PM", "Fee": "Free", "Notes": "First green mall"},
    {"Name": "Magic Planet (Kinfra Park)", "Category": "Entertainment", "Latitude": 8.5786, "Longitude": 76.8732, "Hours": "10:00 AM-6:00 PM", "Fee": "INR 450", "Notes": "Closed on Mondays"},
    {"Name": "Vizhinjam Marine Aquarium", "Category": "Nature", "Latitude": 8.3840, "Longitude": 76.9880, "Hours": "9:00 AM-5:30 PM", "Fee": "INR 20", "Notes": "Image pearl technique"},

    # --- HILL STATIONS & ADVENTURE (Adventurous Vibe) ---
    {"Name": "Ponmudi Hills", "Category": "Hills", "Latitude": 8.7598, "Longitude": 77.1167, "Hours": "6:00 AM-6:00 PM", "Fee": "INR 30", "Notes": "Golden Valley viewpoints"},
    {"Name": "Bonacaud", "Category": "Hills", "Latitude": 8.7500, "Longitude": 77.1800, "Hours": "6:00 AM-5:00 PM", "Fee": "Free", "Notes": "Trekking base camp"},
    {"Name": "Agasthyakoodam", "Category": "Hills", "Latitude": 8.6166, "Longitude": 77.2500, "Hours": "Restricted", "Fee": "Permit Needed", "Notes": "UNESCO Biosphere Reserve"}
]

# Create the Dataframe
df = pd.DataFrame(full_data)

# Export to Excel
filename = "Trivandrum_Travel_Database.xlsx"
df.to_excel(filename, index=False)

print("-" * 30)
print(f"✅ SUCCESS!")
print(f"Total Locations Processed: {len(df)}")
print(f"File Saved As: {filename}")
print("-" * 30)