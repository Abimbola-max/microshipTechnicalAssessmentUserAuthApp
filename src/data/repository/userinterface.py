from abc import ABC, abstractmethod

from src.data.model.user import User


class UserInterface(ABC):

    @abstractmethod
    def save_user(self, user: User):
        pass

    @abstractmethod
    def exists_by_email(self,  email: str) -> bool:
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> User:
        pass

    @abstractmethod
    def find_by_name_or_email(self, name: str, email) -> User:
        pass

    @abstractmethod
    def find_by_name(self, name: str):
        pass

