import pytest
import requests
import json

BASE_URL = "http://localhost:5000/api"

TEST_USER = {
    "username": "testuser",
    "email": "testuser@example.com",
    "password": "Password123!"
}

TEST_PROFILE = {
    "name": "Test User",
    "monthly_income": 50000,
    "monthly_expenses": 20000,
    "risk_appetite": "High",
    "financial_goal": "Retirement",
    "investment_horizon_years": 20
}


def pretty_print(label, response):
    print(f"\n[{label}] Status: {response.status_code}")
    try:
        print(json.dumps(response.json(), indent=2))
    except:
        print(response.text)


def test_signup():
    r = requests.post(f"{BASE_URL}/signup", json=TEST_USER)
    pretty_print("SIGNUP RESPONSE", r)
    assert r.status_code in (200, 201, 400)


@pytest.fixture(scope="session")
def token():
    r = requests.post(f"{BASE_URL}/login", json={
        "email": TEST_USER["email"],
        "password": TEST_USER["password"]
    })
    pretty_print("LOGIN RESPONSE", r)
    assert r.status_code == 200
    t = r.json().get("access_token")
    assert t is not None
    return t


def test_profile(token):
    headers = {"Authorization": f"Bearer {token}"}

    # POST profile
    r = requests.post(f"{BASE_URL}/profile", json=TEST_PROFILE, headers=headers)
    pretty_print("PROFILE POST RESPONSE", r)
    assert r.status_code == 200

    # GET profile
    r2 = requests.get(f"{BASE_URL}/profile", headers=headers)
    pretty_print("PROFILE GET RESPONSE", r2)
    assert r2.status_code == 200
    data = r2.json()
    assert data["name"] == TEST_PROFILE["name"]


def test_recommendation(token):
    headers = {"Authorization": f"Bearer {token}"}

    r = requests.get(f"{BASE_URL}/recommendation", headers=headers)
    pretty_print("RECOMMENDATION RESPONSE", r)
    assert r.status_code == 200
    data = r.json()
    assert "allocation" in data
    assert "expected_returns" in data
    assert "explanation" in data
