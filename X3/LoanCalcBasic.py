class LoanCalcBasic:

    def __init__(self):
        self._principal = None
        self._interest_rate = None
        self._term = None   #stored as Months

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
        sRate = input("Enter interest rate as a decimal.  E.G.: 4.1")
        fRate = -1.0
        while fRate < 0:  #negative interest rates?  maybe not for this trivial exercise...
            fRate = parse_decimal_choice(sRate)
            if fRate < 0.0:
                print("You chose an invalid option.  Choose wisely :-)")
        self._interest_rate = fRate / 100.0

    def get_principal(self):
        fPrincipal = -1.0
        while fPrincipal < 0:
            sPrincipal = input("Enter Principal as a decimal.  E.G.: 42,000")
            fPrincipal = parse_decimal_choice(sPrincipal)
            if fPrincipal < 0.0:
                print("You chose an invalid option.  Choose wisely :-)")
        self._principal = fPrincipal

    def get_term(self):

        sLoanType = ""
        while sLoanType != "home" and sLoanType != "auto":
            sLoanType = input("Is this a Home Loan or Car loan?  E.G.: enter \"Home\" or \"Auto\".").lower()
        nTerm = -1
        sTerm = ""
        if sLoanType == "auto":
            while nTerm < 0:
                sTerm = input("Enter loan term in Months.  E.G.: 60")
                nTerm = parse_int_choice(sTerm)
                if nTerm > 0:
                    break
        elif sLoanType == "home":
            while nTerm < 0:
                sTerm = input("Enter loan term in Years.  E.G.: 30, 15")
                nTerm = parse_int_choice(sTerm) * 12
                if nTerm > 0:
                    break
        self._term = nTerm

    def calc_monthly_payment(self):

        monthly_interest_rate = self._interest_rate / 12.0
        number_of_months = self._term
        numerator = self._principal * monthly_interest_rate
        denominator = (1.0 - ((1.0 + monthly_interest_rate)**(-1 * number_of_months)))
        return numerator / denominator


def parse_decimal_choice(choice):
    try:
        i = float(choice)
        return i
    except ValueError:
        return -1.0


def parse_int_choice(choice):
    try:
        i = int(choice)
        return i
    except ValueError:
        return -1