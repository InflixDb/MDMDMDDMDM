from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["temp_invite_bot"]

# Mongo collections
users_col = db["users"]
channels_col = db["channels"]
requests_col = db["requests"]
