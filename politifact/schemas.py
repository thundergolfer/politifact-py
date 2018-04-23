from marshmallow import Schema, fields, post_load

from politifact.rulings import map_ruling_slug_to_ruling
from politifact.models import Statement


class RulingSchema(Schema):
    ruling = fields.Str()
    ruling_slug = fields.Str()
    canonical_ruling_graphic = fields.URL()


class PartySchema(Schema):
    party = fields.Str()
    party_slug = fields.Str()


class PersonSchema(Schema):
    first_name = fields.Str()
    canonical_photo = fields.URL()
    name_slug = fields.Str()
    party = fields.Nested(PartySchema)


class SubjectsSchema(Schema):
    subject_slug = fields.Str()
    subject = fields.Str()


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


statements_schema = StatementSchema(many=True)
statement_schema = StatementSchema()

subjects_schema = SubjectsSchema(many=True)
persons_schema = PersonSchema(many=True)
rulings_schema = RulingSchema(many=True)
