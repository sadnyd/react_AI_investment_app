from flask import Blueprint, jsonify
import json
import os

market_data_bp = Blueprint('market_data', __name__)

@market_data_bp.route('/marketData', methods=['GET'])
def get_market_data():
    try:
        file_path = os.path.join("static", "market_data.json")
        with open(file_path, "r") as f:
            data = json.load(f)
        return jsonify(data), 200
    except FileNotFoundError:
        return jsonify({"error": "market_data.json not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Failed to parse market_data.json"}), 500
