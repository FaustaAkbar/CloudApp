from pymongo import MongoClient
import os

# Koneksi ke MongoDB
client = MongoClient("mongodb+srv://faussss1357:realmajor@foodordercluster.uys7l.mongodb.net/test?retryWrites=true&w=majority&appName=FoodOrderCluster")
db = client["CloudTugas15"]  # Nama database
collection = db["User"]  # Nama koleksi (tabel)

# Data yang akan dimasukkan ke dalam database
items = [
    {"name": "Item 1", "description": "This is a description for Item 1", "price": 10.99},
    {"name": "Item 2", "description": "This is a description for Item 2", "price": 20.50},
    {"name": "Item 3", "description": "This is a description for Item 3", "price": 15.75},
    {"name": "Item 4", "description": "This is a description for Item 4", "price": 8.99},
]

# Menambahkan data ke dalam koleksi
collection.insert_many(items)

print("Data berhasil disimpan!")
