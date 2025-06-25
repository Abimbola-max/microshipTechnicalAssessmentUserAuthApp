from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError

from src.data.model.user import User
from src.dto.request.loginrequest import UserLoginRequest
from src.dto.request.registrationrequest import UserRegRequest
from src.service.userservices.userservice import UserService


class UserController:

    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def register(self):
        data = request.get_json()
        try:
            user_data_request = UserRegRequest().load(data)
            response_data = self.user_service.register(user_data_request)
            return jsonify(response_data), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    def login(self):
        try:
            data = request.get_json()
            user_login_request = UserLoginRequest().load(data)
            response = self.user_service.login(user_login_request)
            return jsonify(response), 200
        except ValidationError as e:
            return jsonify({"error": e.messages}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 400



