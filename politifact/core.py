from hammock import Hammock

from politifact.schemas import statements_schema


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
        first_name, second_name = name.lower().split()
        person_slug = '{}-{}'.format(first_name, second_name)
        resp = self.root.people(person_slug).json().GET()
        stmts = resp.json()
        # return [statement_schema.load(elem).data for elem in stmts]
        return statements_schema.load(stmts).data

    def rulings(self, ruling, n=None):
        return self.root.rulings(ruling).json().GET()

    def detail(self, id):
        # TODO: check id is an int
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
