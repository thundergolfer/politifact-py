from politifact import Politifact, Statement
from politifact import rulings


class TestPolitifact():
    poli = Politifact()

    def test_one_equals_one(self):
        assert 1 == 1

    def test_statements_by_person(self):
        stmts = self.poli.statements().people('barack obama')
        assert all(isinstance(x, Statement) for x in stmts)

    def test_statements_by_ruling(self):
        stmts = self.poli.statements().rulings(rulings.MOSTLY_FALSE)
        assert all(isinstance(x, Statement) for x in stmts)

    def test_statement_detail(self):
        stmt_id = 125
        stmt = self.poli.statements().detail(stmt_id)
        assert isinstance(stmt, Statement)
