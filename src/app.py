import os
from datetime import timedelta

from dotenv import load_dotenv
from flasgger import Swagger
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required, get_jwt_identity


from src.controller.usercontroller import UserController
from src.data.repository.userrespository import UserRepository
from src.dto.response.profileresponse import ProfileResponse
from src.exceptions.exception import NotFoundException
from src.service.userservices.userservice import UserService

app = Flask(__name__)

load_dotenv()
Swagger(app)

app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config['JWT_TOKEN_LOCATION'] = ['headers']
app.config['JWT_HEADER_NAME'] = 'Authorization'
app.config['JWT_HEADER_TYPE'] = 'Bearer'
profile_response = ProfileResponse()

jwt = JWTManager(app)

mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
db_name = os.getenv("DATABASE_NAME", "User_Authentication")

user_repo = UserRepository(mongo_uri, db_name)
user_service = UserService(user_repo)
user_controller = UserController(user_service)

@app.route('/register', methods=['POST'])
def register():
    return user_controller.register()

@app.route('/login', methods=['POST'])
def login():
    return user_controller.login()


@app.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    current_user_email = get_jwt_identity()
    try:
        user = user_repo.find_by_email(current_user_email)
        return jsonify(profile_response.dump(user)), 200
    except NotFoundException as e:
        return jsonify({'error': str(e)}), 404



if __name__ == '__main__':
    app.run(debug=True)
