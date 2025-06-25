class NotFoundException(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class EmailAlreadyExistException(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class InvalidDetailsException(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class ProfileDoesNotExistException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class NullException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidEmailPatternException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidNameLengthException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidNameException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class VerificationFailedException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)



