from marshmallow import Schema, fields, validate, ValidationError, validates
from marshmallow.validate import Email

class UserLoginRequest(Schema):
    email_or_name = fields.Str(required=True, validate=validate.Length(min=1))
    password = fields.Str(required=True, validate=validate.Length(min=1))

    @validates('email_or_name')
    def validate_email_or_name(self, value, **kwargs):
        if '@' in value:
            try:
                Email()(value)
            except ValidationError:
                raise ValidationError("Invalid email format")
        else:
            if not (3 <= len(value) <= 50):
                raise ValidationError("Name must be 3–50 characters long")
