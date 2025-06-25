from pymongo import MongoClient

from src.data.model.user import User
from src.data.repository.userinterface import UserInterface
from src.exceptions.exception import NotFoundException


class UserRepository(UserInterface):

    def __init__(self, mongo_uri, db_name):
        self.client = MongoClient(mongo_uri)
        self.database = self.client[db_name]
        self.collection = self.database['users']

    def save_user(self, user: User):
        user_data = {
            "name": user.name,
            "email": user.email,
            "password": user.password
        }
        insert_result = self.collection.insert_one(user_data)
        user.user_data = str(insert_result.inserted_id)
        return user

    def exists_by_email(self,  email: str) -> bool:
        return self.collection.find_one({"email": email}) is not None

    def find_by_email(self, email: str) -> User:
        data = self.collection.find_one({'email': email})
        if not data:
            raise NotFoundException("User not Found.")
        return User(**data)

    def find_by_name_or_email(self, name: str, email) -> User:
        data = self.collection.find_one({"name": name, "email": email})
        if not data:
            raise NotFoundException("User not Found.")
        return User(**data)

    def find_by_name(self, name: str):
        data = self.collection.find_one({'name': name})
        if not data:
            raise NotFoundException("User not Found.")
        return User(**data)
