from datetime import timedelta

from flask_jwt_extended import create_access_token

from src.data.model.user import User
from src.data.repository.userrespository import UserRepository
from src.dto.request.registrationrequest import UserRegRequest
from src.dto.response.registrationresponse import UserRegResponse
from src.exceptions.exception import *
from src.service.passwordsecurity.passwordencrypt import PasswordEncrypt


class UserService:

    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo
        self.user_schema = UserRegRequest()

    def register(self, user_reg_request):
        if self.user_repo.exists_by_email(user_reg_request['email']):
            raise EmailAlreadyExistException("A user with this email already exists.")
        hashed_password = PasswordEncrypt.encrypt_password(user_reg_request["password"])
        user = User (
            name = user_reg_request["name"],
            email = user_reg_request["email"],
            password=hashed_password
        )
        saved_user = self.user_repo.save_user(user)
        response = {
            "message": f"Dear {saved_user.name}, you have registered Successfully.",
        }
        return UserRegResponse().dump(response)

    def login(self, user_login_request):
        email_or_name = user_login_request.get("email_or_name")
        password = user_login_request["password"].strip()

        user = None
        if '@' in email_or_name:
            user = self.user_repo.find_by_email(email_or_name)
        else:
            user = self.user_repo.find_by_name(email_or_name)

        if not user:
            raise NotFoundException("User not found")

        if not PasswordEncrypt.verify_password(password, user.password):
            raise InvalidDetailsException("Invalid credentials")

        access_token = create_access_token(
            identity=str(user.email),
            expires_delta=timedelta(hours=1)
        )

        return {
            "message": f"Hello '{user.name}' you have successfully logged in.",
            "access_token": access_token
        }
