from pymongo import MongoClient
import os
from datetime import datetime

client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017"))
db = client["chat_crm"]
users = db["users"]
messages = db["messages"]

_conversations = {}

def create_user(user):
    user_id = user.get("user_id")
    if not user_id:
        return {"error": "user_id is required"}
    users.replace_one({"user_id": user_id}, user, upsert=True)
    return {"status": "created", "user_id": user_id}

def update_user(user_id, user):
    users.update_one({"user_id": user_id}, {"$set": user})
    return {"status": "updated"}

def save_chat_message(user_id, message, response):
    messages.insert_one({
        "user_id": user_id,
        "message": message,
        "response": response,
        "timestamp": datetime.utcnow()
    })

def save_conversation(user_id: str, user_message: str, bot_response: str):
    if user_id not in _conversations:
        _conversations[user_id] = []
    _conversations[user_id].append({
        "timestamp": datetime.utcnow().isoformat(),
        "user_message": user_message,
        "bot_response": bot_response
    })

def get_conversations(user_id: str):
    return {
        "user_id": user_id,
        "history": _conversations.get(user_id, [])
    }
def get_user_by_id(user_id):
    return users.find_one({"user_id": user_id})
