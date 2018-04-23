from hammock import Hammock

from politifact.schemas import statements_schema, subjects_schema, persons_schema, rulings_schema
from politifact.util import parse_name_str, slugify
from politifact.rulings import Ruling


class Person():
    def __init__(self, politifact, firstname, lastname):
        self.politifact = politifact
        self.firstname = firstname
        self.lastname = lastname

    @property
    def slug(self):
        return self.firstname + '-' + self.lastname


class StatementsEndpoint():
    def __init__(self, root):
        self.root = root.statements(Politifact.EDITION)

    def people(self, name, n=None):
        first_name, second_name = parse_name_str(name)
        person_slug = slugify(first_name, second_name)
        resp = self.root.people(person_slug).json().GET()
        stmts = resp.json()
        return statements_schema.load(stmts).data

    def rulings(self, ruling, n=None):
        if not isinstance(ruling, Ruling):
            raise ValueError("'ruling' parameter must be instance of {}".format(Ruling))
        resp = self.root.rulings(ruling).json().GET()
        stmts = resp.json()
        return statements_schema.load(stmts).data

    def detail(self, id):
        try:
            id = int(id)
        except ValueError:
            raise ValueError('must provide the integer ID of a statement')

        return self.root.detail(id).json().GET()


class PromisesEndpoint():
    def __init__(self, root):
        self.root = root

    def group(self, group_name, subject=None, n=None):
        if not subject:
            return getattr(self.root, group_name)().json().GET()
        else:
            return getattr(self.root, group_name)().subjects(subject).json().GET()


class UpdatesEndpoint():
    def __init__(self, root):
        self.root = root

    def group(self, group_name, subject=None, n=None):
        if not subject:
            return getattr(self.root, group_name)().json().GET()
        else:
            return getattr(self.root, group_name)().subjects(subject).json().GET()


class SubjectsEndpoint():
    def __init__(self, politifact):
        self.politifact = politifact

    def all(self):
        resp = self.politifact.root.subjects().all().json().GET()
        data = resp.json()

        return subjects_schema.load(data).data


class PeopleEndpoint():
    def __init__(self, politifact):
        self.politifact = politifact

    def all(self):
        resp = self.politifact.root.people().all().json().GET()
        data = resp.json()

        return persons_schema.load(data).data


class RulingsEndpoint():
    def __init__(self, politifact):
        self.politifact = politifact

    def all(self):
        resp = self.politifact.root.rulings().all().json().GET()
        data = resp.json()

        return rulings_schema.load(data).data


class Politifact():
    API_ROOT = 'http://www.politifact.com/api'
    EDITION = 'truth-o-meter'

    def __init__(self):
        self.root = Hammock(self.API_ROOT)

    def statements(self):
        return StatementsEndpoint(self.root)

    def promises(self):
        return PromisesEndpoint(self.API_ROOT)

    def stories(self, n=None):
        full_endpoint = self.root.stories().json()
        if n:
            full_endpoint += '?n={}'.format(n)
        return full_endpoint.GET()

    def updates(self):
        return UpdatesEndpoint(self.API_ROOT)

    def subjects(self):
        return SubjectsEndpoint(self)

    def people(self):
        return PeopleEndpoint(self)

    def rulings(self):
        return RulingsEndpoint(self)
