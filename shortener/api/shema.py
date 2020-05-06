from marshmallow import Schema, fields


class CreateShortSchema(Schema):
    url = fields.Url(required=True)


class CreateShortResponseShema(Schema):
    short = fields.Str(required=True)
