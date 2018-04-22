from politifact import Politifact, Statement


class TestPolitifact():
    poli = Politifact()

    def test_one_equals_one(self):
        assert 1 == 1

    def test_statements_by_person(self):
        stmts = self.poli.statements().people('barack obama')
        assert all(isinstance(x, Statement) for x in stmts)
