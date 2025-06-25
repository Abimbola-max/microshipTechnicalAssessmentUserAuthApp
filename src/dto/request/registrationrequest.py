from marshmallow import fields, Schema, validate


class UserRegRequest(Schema):
    name = fields.Str(required=True, allow_none=False, validate=validate.Length(min=1))
    email = fields.Email(required=True, allow_none=False, validate=validate.Email())
    password = fields.Str(required=True, allow_none=False, validate=validate.Length(min=8))