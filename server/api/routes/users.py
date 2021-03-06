import secrets
from datetime import datetime

from flask import Blueprint, jsonify, make_response, request
from flask_api import status

from ..db import db_users, db_sessions
from ..security.sec_utils import (check_hash, generate_hash, generate_token,
                                  token_required, api_key_required)

users = Blueprint('/api/users', __name__)

@users.route("/api/users", methods=["GET"])
@api_key_required
def get_users():
    userId = None

    if request.args:
        userId = request.args["userId"]    
        
        if userId:        
            user = db_users.get_user_by_id(userId)             
            if user:
                return make_response(jsonify(user), 200)
            else:
                return make_response(jsonify({"message": "User not found"}), 404)
    else:
        result = db_users.get_all_users()
        if result:
            return make_response(jsonify(result), 200)
        else:                
            return make_response(jsonify({"message": "No results found"}), 404)

@users.route("/api/users", methods=["POST"])
@api_key_required
def create_user():
    try:
        data = request.get_json()
        username = data["username"]
        raw_password = data["password"]
        password = generate_hash(raw_password.encode('utf8'))

        try:
            user_exists = db_users.get_user_by_username(username)
            if user_exists:                
                return make_response(jsonify({"message": "Username or password taken"}), 400)
        except:
            pass            
    except:
        return make_response(jsonify({"message": "Incorrect data"}), 400)
    else:
        db_users.create_user(username, password)
        new_user = db_users.get_user_by_username(username)
        token = generate_token(new_user[0]["Id"])
        db_sessions.log_user_in(new_user[0]["Id"])
        new_user[0].update({"loginToken": token})
        return make_response(jsonify(new_user), 201)

@users.route("/api/users", methods=["PATCH"])
@api_key_required
@token_required
def update_user(user_id):
    data = request.get_json()
    allowed_fields = {"username", "password"}
    new_data = dict(filter(lambda elem: elem[0] in allowed_fields, data.items()))

    if new_data:
        if new_data.get("password"):
            new_data["password"] = generate_hash(new_data.pop("password").encode('utf8'))
        db_users.update_user(user_id, new_data)
    else:
        return make_response(jsonify({"message": "Incorrect data"}), 400)

    return make_response(jsonify({"message": "User updated"}), 200)
    
@users.route("/api/users", methods=["DELETE"])
@api_key_required
@token_required
def delete_user(user_id):
    data = request.get_json()
    password_claim = data["password"].encode('utf8')
    stored_password = db_users.get_user_password(user_id)

    if check_hash(password_claim, stored_password):
        db_users.delete_user(user_id)
        return "", status.HTTP_204_NO_CONTENT
    else:    
        return make_response(jsonify({"message": "Could not authenticate"}), 400)