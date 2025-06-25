from marshmallow import Schema, fields


class UserRegResponse(Schema):

    message = fields.Str()