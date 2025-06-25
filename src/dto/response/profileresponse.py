from marshmallow import Schema, fields


class ProfileResponse(Schema):
    name = fields.Str()
    email = fields.Email()