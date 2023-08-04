from flask import jsonify, request
from models.user_model import UserModel
from app import app
from schema.user_schema import UserSchema
from bson import ObjectId

user_obj = UserModel()
user_schema = UserSchema()

@app.route('/users', methods=['GET'])
def get_all_users():
    users = user_obj.find_all_users()
    return jsonify(users)

@app.route('/users/<string:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = user_obj.find_user_by_id(ObjectId(user_id))
    if user:
        return jsonify(user)
    else:
        return jsonify({"message": "User not found"}), 404 

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    errors = user_schema.validate(data)
    if errors:
        return jsonify({"message": "Validation errors", "errors": errors}), 400

    user_id = user_obj.create_user(data)
    return jsonify({"message": "User created successfully", "user_id": user_id}), 201

@app.route('/users/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    errors = user_schema.validate(data)
    if errors:
        return jsonify({"message": "Validation errors", "errors": errors}), 400

    updated = user_obj.update_user_by_id(ObjectId(user_id), data)
    if updated:
        return jsonify({"message": "User updated successfully"})
    else:
        return jsonify({"message": "User not found"}), 404

@app.route('/users/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    deleted = user_obj.delete_user_by_id(ObjectId(user_id))
    if deleted:
        return jsonify({"message": "User deleted successfully"})
    else:
        return jsonify({"message": "User not found"}), 404
