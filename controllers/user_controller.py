from flask_restful import Resource, reqparse
from models.user_model import UserModel
from schema.user_schema import UserSchema
from flask import jsonify
from bson import ObjectId

user_obj = UserModel()
user_schema = UserSchema()

class UserResource(Resource):
    def get(self, user_id=None):
        if user_id:
            try:
                user = user_obj.find_user_by_id(ObjectId(user_id))
            except Exception as e:
                return {"message": "Error fetching user", "error": str(e)}, 500

            if user:
                return user_schema.dump(user), 200
            else:
                return {"message": "User not found"}, 404

        try:
            users = user_obj.find_all_users()
            # print("in user_controller",users)
        except Exception as e:
            return {"message": "Error fetching users", "error": str(e)}, 500

        return user_schema.dump(users, many=True), 200

    def post(self):
        data = reqparse.request.get_json()
        #print(data)
        errors = user_schema.validate(data)
        if errors:
            return {"message": "Validation errors", "errors": errors}, 400

        try:
            user_id = user_obj.create_user(data)
        except Exception as e:
            return {"message": "Error creating user", "error": str(e)}, 500

        return {"message": "User created successfully", "user_id": user_id}, 201

    def put(self, user_id):
        data = reqparse.request.get_json()
        errors = user_schema.validate(data)
        if errors:
            return {"message": "Validation errors", "errors": errors}, 400

        try:
            updated = user_obj.update_user_by_id(ObjectId(user_id), data)
        except Exception as e:
            return {"message": "Error updating user", "error": str(e)}, 500

        if updated:
            return {"message": "User updated successfully"}, 200
        else:
            return {"message": "User not found"}, 404

    def delete(self, user_id):
        try:
            deleted = user_obj.delete_user_by_id(ObjectId(user_id))
        except Exception as e:
            return {"message": "Error deleting user", "error": str(e)}, 500

        if deleted:
            return {"message": "User deleted successfully"}, 200
        else:
            return {"message": "User not found"}, 404
