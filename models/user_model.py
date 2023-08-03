from bson import ObjectId
from pymongo import MongoClient
from configs.config import dbconfig

class UserModel:
    def __init__(self):
        self.client = MongoClient(host=dbconfig['host'], port=dbconfig['port'])
        self.db = self.client[dbconfig['database']]
        self.collection = self.db['users']

    def find_all_users(self):
        users = list(self.collection.find())
        for user in users:
            user['_id'] = str(user['_id'])
        return users

    def find_user_by_id(self, user_id):
        user = self.collection.find_one({"id": user_id})
        if user:
            user['_id'] = str(user['_id'])
        return user

    def create_user(self, data):
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

    def update_user_by_id(self, user_id, data):
        result = self.collection.update_one({"id": user_id}, {"$set": data})
        return result.modified_count > 0

    def delete_user_by_id(self, user_id):
        result = self.collection.delete_one({"id": user_id})
        return result.deleted_count > 0
