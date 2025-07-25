from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson.objectid import ObjectId
import json
import os

agent_bp = Blueprint('agent', __name__)

@agent_bp.route('/recommendation', methods=['GET'])
@jwt_required()
def get_recommendation():
    db = current_app.config["DB"]
    user_id = get_jwt_identity()

    profile = db.profiles.find_one({"user_id": ObjectId(user_id)})
    if not profile:
        return jsonify({"msg": "Profile not found"}), 404

    # Load market data
    # market_data_path = os.path.join(current_app.root_path, 'static', 'market_data.json')
    with open('static/market_data.json') as f:
        market_data = json.load(f)

    risk = profile["risk_appetite"].lower()
    allocation = {}

    if risk == "high":
        allocation = {"stocks": 70, "mutual_funds": 20, "fixed_deposits": 10}
    elif risk == "medium":
        allocation = {"stocks": 40, "mutual_funds": 40, "fixed_deposits": 20}
    elif risk == "low":
        allocation = {"stocks": 10, "mutual_funds": 40, "fixed_deposits": 50}
    else:
        return jsonify({"msg": "Invalid risk appetite"}), 400

    expected_returns = {
        "stocks": market_data["stocks"][0]["growth_pct_yoy"],  # Simplified
        "mutual_funds": market_data["mutual_funds"][0]["return_pct_3y_cagr"],
        "fixed_deposits": market_data["fixed_deposits"][0]["rate_pct"]
    }

    explanation = f"Based on your {risk} risk appetite, " \
                  f"your portfolio should have {allocation['stocks']}% in stocks, " \
                  f"{allocation['mutual_funds']}% in mutual funds, " \
                  f"and {allocation['fixed_deposits']}% in fixed deposits. " \
                  f"This balances risk and returns according to your profile."

    response = {
        "allocation": allocation,
        "expected_returns": expected_returns,
        "explanation": explanation,
        "market_data": market_data
    }

    return jsonify(response)
