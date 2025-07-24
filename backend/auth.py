from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import create_access_token
from bson.objectid import ObjectId
import bcrypt

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    db = current_app.config["DB"]
    data = request.json

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not all([username, email, password]):
        return jsonify({"msg": "Missing fields"}), 400

    existing_user = db.users.find_one({"email": email})
    if existing_user:
        return jsonify({"msg": "User already exists"}), 400

    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    db.users.insert_one({
        "username": username,
        "email": email,
        "password": hashed_pw
    })

    return jsonify({"msg": "User created"}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    db = current_app.config["DB"]
    data = request.json

    email = data.get("email")
    password = data.get("password")

    user = db.users.find_one({"email": email})
    if not user:
        return jsonify({"msg": "Invalid credentials"}), 401

    if not bcrypt.checkpw(password.encode('utf-8'), user["password"]):
        return jsonify({"msg": "Invalid credentials"}), 401

    access_token = create_access_token(identity=str(user["_id"]))

    return jsonify(access_token=access_token), 200
