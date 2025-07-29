# routes/profile_get.py

from flask import Blueprint, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson.objectid import ObjectId

profile_get_bp = Blueprint('profile_get', __name__)

@profile_get_bp.route('/profile/fetch', methods=['GET'])
@jwt_required()
def get_user_profile():
    db = current_app.config["DB"]
    user_id = get_jwt_identity()

    profile = db.profiles.find_one({"user_id": ObjectId(user_id)})
    if not profile:
        return jsonify({"msg": "Profile not found"}), 404

    # Convert ObjectId to string
    profile["_id"] = str(profile["_id"])
    profile["user_id"] = str(profile["user_id"])

    return jsonify(profile), 200
