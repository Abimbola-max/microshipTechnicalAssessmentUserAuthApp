import bcrypt

class PasswordEncrypt:

    @staticmethod
    def encrypt_password(password: str):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

    @staticmethod
    def verify_password(password: str, hashed_password: str):

        return bcrypt.checkpw(
            password.encode('utf-8'),
            hashed_password.encode('utf-8')
        )


