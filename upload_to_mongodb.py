import pandas as pd
from pymongo import MongoClient

# 1. Setup Connection (Update the string if using MongoDB Atlas)
client = MongoClient("mongodb+srv://devisumanair_db_user:Devi%402003@surveydata.9ohe7ek.mongodb.net/?appName=SurveyData")
db = client["Trivandrum_Travel_Database"]
collection = db["locations"]

# 2. Load the Excel data
try:
    df = pd.read_excel("Trivandrum_Travel_Database.xlsx")
    
    # 3. Convert to dictionary and upload
    data_to_upload = df.to_dict("records")
    collection.insert_many(data_to_upload)
    
    print(f"🚀 SUCCESS: {len(data_to_upload)} locations are now LIVE in your MongoDB!")
except Exception as e:
    print(f"❌ ERROR: {e}")
    # ... inside your upload script ...
df = pd.read_excel("Trivandrum_Travel_Database.xlsx")
print(f"Rows found in Excel: {len(df)}") # ADD THIS

data_dict = df.to_dict("records")
print(f"Sample data: {data_dict[0]}") # ADD THIS

collection.insert_many(data_dict)
print("Upload complete!")
# ... (inside your upload script, after connecting to collection)
    
    # 3. Clear old data so we don't have duplicates!
collection.delete_many({}) 
    
    # 4. Upload
data_dict = df.to_dict("records")
collection.insert_many(data_dict)
    
print(f"🚀 SUCCESS: {len(data_dict)} fresh locations are LIVE!")