from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
import os

app = FastAPI()

# Koneksi ke MongoDB
client = MongoClient(os.getenv("MONGODB_URI"))
db = client["CloudTugas15"]
collection = db["User"]  # Mendefinisikan koleksi "User"

@app.get("/")
def read_root():
    return {"message": "Welcome to the scalable app!"}

@app.post("/data")
def save_data(item: dict):
    try:
        # Menggunakan collection yang sudah didefinisikan
        collection.insert_one(item)
        return {"message": "Data saved!", "data": item}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving data: {e}")

@app.get("/data")
def get_data():
    try:
        # Menggunakan collection yang sudah didefinisikan
        data = list(collection.find({}, {"_id": 0}))
        return {"data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching data: {e}")
