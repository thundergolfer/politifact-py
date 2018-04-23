
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


class Ruling():
    def __init__(self, name, slug, graphic):
        self.name = name
        self.slug = slug
        self.graphic = graphic

    def __str__(self):
        return self.name
