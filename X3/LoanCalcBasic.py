class LoanCalcBasic:

    def __init__(self):
        self._principal = None
        self._interest_rate = None
        self._term = None

    @property
    def principal(self):
        return self._principal

    @principal.setter
    def principal(self, value):
        self._principal = value

    @property
    def interest_rate(self):
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, value):
        self._interest_rate = value

    @property
    def term(self):
        return self._term

    @term.setter
    def term(self, value):
        self._term = value

    def get_interest_rate(self):
        return 1