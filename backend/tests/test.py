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
    "financial_goal": "Retirement"
}

test_log = {
    "user_creation": {},
    "profile_creation": {},
    "profile_fetch": {}
}


def test_create_user():
    response = requests.post(f"{BASE_URL}/users", json=TEST_USER)
    test_log["user_creation"]["sent"] = TEST_USER
    test_log["user_creation"]["received"] = response.json()
    test_log["user_creation"]["status_code"] = response.status_code
    assert response.status_code == 201


def test_create_profile():
    response = requests.post(f"{BASE_URL}/profile", json=TEST_PROFILE)
    test_log["profile_creation"]["sent"] = TEST_PROFILE
    test_log["profile_creation"]["received"] = response.json()
    test_log["profile_creation"]["status_code"] = response.status_code
    assert response.status_code == 201


def test_get_profile():
    response = requests.get(f"{BASE_URL}/profile")
    test_log["profile_fetch"]["received"] = response.json()
    test_log["profile_fetch"]["status_code"] = response.status_code
    assert response.status_code == 200


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_teardown(item):
    """After all tests, write the log to JSON."""
    yield
    with open("tests/test_output.json", "w") as f:
        json.dump(test_log, f, indent=4)
