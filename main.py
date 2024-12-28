from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

# Koneksi ke MongoDB
client = MongoClient("mongodb+srv://faussss1357:realmajor@foodordercluster.uys7l.mongodb.net/test?retryWrites=true&w=majority&appName=FoodOrderCluster")
db = client["CloudTugas15"]

@app.get("/")
def read_root():
    return {"message": "Welcome to the scalable app!"}

@app.post("/data")
def save_data(item: dict):
    db.collection.insert_one(item)
    return {"message": "Data saved!", "data": item}

@app.get("/data")
def get_data():
    data = list(db.collection.find({}, {"_id": 0}))
    return {"data": data}
