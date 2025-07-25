from flask import Flask, Response, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import subprocess


from routes.auth import auth_bp
from routes.profile import profile_bp
from routes.agent import agent_bp


load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return {
        "message": "Smart Financial Advisor API is running!",
        "endpoints": [
            "/api/health",
            "/api/db-test",
            "/api/auth",
            "/api/profile",
            "/api/agent"
        ]
    }, 200

    
@app.route("/health", methods=["GET"])
def health():
    try:
        # Use pytest as subprocess
        result = subprocess.run(
            ["pytest", "tests/test.py", "--tb=short", "-q"],
            capture_output=True,
            text=True,
            check=True
        )
        return Response(result.stdout, mimetype="text/plain"), 200
    except subprocess.CalledProcessError as e:
        return Response(
            f"Health check failed:\n{e.stdout}\n{e.stderr}",
            mimetype="text/plain"
        ), 500



# Configure JWT secret key from environment
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
jwt = JWTManager(app)


mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db_name = os.getenv("MONGO_DB_NAME", "smart_financial_advisor")
db = client[db_name]

# Register blueprints
app.register_blueprint(auth_bp, url_prefix="/api")
app.register_blueprint(profile_bp, url_prefix="/api")
app.register_blueprint(agent_bp, url_prefix="/api")

# Make DB accessible in blueprints
app.config["DB"] = db



if __name__ == "__main__":
    app.run(debug=True)
