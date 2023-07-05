class Transaction:
    def __int__(self, id_, state, date, amount, name_currency, code_currency):
        self.id = id_
        self.state = state
        self.date = date
        self.amount = amount
        self.name_currency = name_currency
        self.code_curency = code_currency
