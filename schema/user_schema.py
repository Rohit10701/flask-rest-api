from marshmallow import Schema, fields

class UserSchema(Schema):
    _id = fields.Str(attribute="_id")
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)
