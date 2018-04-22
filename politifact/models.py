from marshmallow import Schema, fields, post_load

from politifact.rulings import map_ruling_slug_to_ruling


class PartySchema(Schema):
    party = fields.Str()
    party_slug = fields.Str()


class PersonSchema(Schema):
    first_name = fields.Str()
    canonical_photo = fields.URL()
    name_slug = fields.Str()
    party = fields.Nested(PartySchema)


class StatementSchema(Schema):
    statement_date = fields.Str()
    statement = fields.Str()
    speaker = fields.Nested(PersonSchema)
    statement_context = fields.Str()
    subjects = fields.List(fields.Dict())
    ruling_date = fields.DateTime()
    statement_type = fields.Dict()
    ruling_link_text = fields.Str()
    ruling_headline = fields.Str()
    ruling = fields.Function(lambda obj: map_ruling_slug_to_ruling(obj))
    statement_url = fields.Str()

    @post_load
    def make_statement(self, data):
        return Statement(**data)


class Statement():
    def __init__(
        self,
        statement_date,
        statement,
        speaker,
        statement_context,
        ruling_date,
        statement_type,
        ruling_link_text,
        ruling_headline,
        ruling,
        statement_url,
        subjects=None
    ):
        self.statement_date = statement_date
        self.statement = statement
        self.speaker = speaker
        self.statement_context = statement_context
        self.ruling_date = ruling_date
        self.statement_type = statement_type
        self.ruling_link_text = ruling_link_text
        self.ruling_headline = ruling_headline
        self.ruling = ruling
        self.statement_url = statement_url
        self.subjects = subjects


statements_schema = StatementSchema(many=True)
statement_schema = StatementSchema()
