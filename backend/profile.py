from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson.objectid import ObjectId

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile', methods=['POST'])
@jwt_required()
def create_profile():
    db = current_app.config["DB"]
    user_id = get_jwt_identity()
    data = request.json

    # Validate required fields
    required_fields = [
        "name", "monthly_income", "monthly_expenses",
        "risk_appetite", "financial_goal", "investment_horizon_years"
    ]
    if not all(field in data for field in required_fields):
        return jsonify({"msg": "Missing profile fields"}), 400

    profile = {
        "user_id": ObjectId(user_id),
        "name": data["name"],
        "monthly_income": data["monthly_income"],
        "monthly_expenses": data["monthly_expenses"],
        "risk_appetite": data["risk_appetite"],
        "financial_goal": data["financial_goal"],
        "investment_horizon_years": data["investment_horizon_years"]
    }

    existing = db.profiles.find_one({"user_id": ObjectId(user_id)})
    if existing:
        db.profiles.update_one({"user_id": ObjectId(user_id)}, {"$set": profile})
    else:
        db.profiles.insert_one(profile)

    return jsonify({"msg": "Profile saved"}), 200


@profile_bp.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    db = current_app.config["DB"]
    user_id = get_jwt_identity()

    profile = db.profiles.find_one({"user_id": ObjectId(user_id)})
    if not profile:
        return jsonify({"msg": "Profile not found"}), 404

    profile["_id"] = str(profile["_id"])
    profile["user_id"] = str(profile["user_id"])
    return jsonify(profile)
