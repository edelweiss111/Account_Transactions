from datetime import datetime


class Transaction:
    def __init__(self, id_, state, date_, amount, name_currency, code_currency, description, sender, recipient):
        """
        Инициализация полей класса
        """
        self.id = id_
        self.state = state
        self.date = date_
        self.amount = amount
        self.name_currency = name_currency
        self.code_currency = code_currency
        self.description = description
        self.sender = sender
        self.recipient = recipient

    def __repr__(self):
        """
        Экземпляр возвращает свой id при вызове
        """
        return f'Транзакция {self.id}'

    def get_date(self):
        """
        Возвращает дату выполнения транзакции в нужном формате
        """
        date_ = datetime.fromisoformat(self.date)
        return date_.strftime("%d.%m.%Y")

    def hiding_sender(self):
        """
        Возвращает скрытый номер отправителя
        """
        # Отделяет номер счета/карты от коментария
        number = ''
        for symbol in self.sender:
            if symbol.isdigit():
                number += symbol
        # Если это номер карты
        if len(number) == 16:
            hiding_card = '** **** '
            return number[:4] + ' ' + number[4:6] + hiding_card + number[-4:]
        # Если это номер счета
        else:
            hiding_account = '**'
            return hiding_account + number[-4:]




