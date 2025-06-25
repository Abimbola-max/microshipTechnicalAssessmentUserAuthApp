class User:
    def __init__(self, name, email, password, _id=None):
        self.name = name
        self.email = email
        self.password = password
        self._id = _id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password