from flask import Blueprint, jsonify, current_app
import requests

health_bp = Blueprint('health_bp', __name__)

BASE_URL = "http://localhost:5000/api"

TEST_USER = {
    "username": "healthcheck_user",
    "email": "healthcheck@example.com",
    "password": "TestPass123!"
}

TEST_PROFILE = {
    "name": "Health Check",
    "monthly_income": 60000,
    "monthly_expenses": 25000,
    "risk_appetite": "Moderate",
    "financial_goal": "Wealth Creation",
    "investment_horizon_years": 10
}


@health_bp.route("/health", methods=["GET"])
def health_check():
    result = {}

    # Test signup
    try:
        signup_resp = requests.post(f"{BASE_URL}/signup", json=TEST_USER)
        result["signup"] = {
            "status_code": signup_resp.status_code,
            "response": safe_json(signup_resp)
        }
    except Exception as e:
        result["signup"] = {"error": str(e)}

    # Test login
    try:
        login_resp = requests.post(f"{BASE_URL}/login", json={
            "email": TEST_USER["email"],
            "password": TEST_USER["password"]
        })
        token = login_resp.json().get("access_token")
        result["login"] = {
            "status_code": login_resp.status_code,
            "response": login_resp.json()
        }
    except Exception as e:
        result["login"] = {"error": str(e)}
        token = None

    headers = {"Authorization": f"Bearer {token}"} if token else {}

    # POST profile
    try:
        post_profile = requests.post(f"{BASE_URL}/profile", json=TEST_PROFILE, headers=headers)
        result["profile_post"] = {
            "status_code": post_profile.status_code,
            "response": safe_json(post_profile)
        }
    except Exception as e:
        result["profile_post"] = {"error": str(e)}

    # GET profile
    try:
        get_profile = requests.get(f"{BASE_URL}/profile", headers=headers)
        result["profile_get"] = {
            "status_code": get_profile.status_code,
            "response": safe_json(get_profile)
        }
    except Exception as e:
        result["profile_get"] = {"error": str(e)}

    # Recommendation
    try:
        rec_resp = requests.get(f"{BASE_URL}/recommendation", headers=headers)
        result["recommendation"] = {
            "status_code": rec_resp.status_code,
            "response": safe_json(rec_resp)
        }
    except Exception as e:
        result["recommendation"] = {"error": str(e)}

    return jsonify(result)


def safe_json(response):
    try:
        return response.json()
    except:
        return response.text
