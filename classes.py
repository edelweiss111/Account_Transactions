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
        Возвращает информацию о транзакции в нужном виде
        """
        return f'{self.get_date() + self.description}\n' \
               f'{self.hiding_sender() + self.hiding_recipient()}\n' \
               f'{self.get_currency()}\n'

    def get_date(self):
        """
        Возвращает дату выполнения транзакции в нужном формате
        """
        date_ = datetime.fromisoformat(self.date)
        return date_.strftime("%d.%m.%Y ")

    def hiding_sender(self):
        """
        Возвращает скрытый номер отправителя
        """
        # Отделяет номер счета/карты от названия карты/счета
        number = ''
        title = ''
        for symbol in self.sender:
            if symbol.isdigit():
                number += symbol
            else:
                title += symbol
        # Если это номер карты
        if len(number) == 16:
            hiding_card = '** **** '
            return title + number[:4] + ' ' + number[4:6] + hiding_card + number[-4:] + ' -> '
        # Если это номер счета
        elif len(number) == 20:
            hiding_account = '**'
            return title + hiding_account + number[-4:] + ' -> '
        # Если отправитель отсутствует
        else:
            return '-> '

    def hiding_recipient(self):
        """
        Возвращает скрытый номер получателя
        """
        # Отделяет номер счета/карты от названия карты/счета
        number = ''
        title = ''
        for symbol in self.recipient:
            if symbol.isdigit():
                number += symbol
            else:
                title += symbol
        # Если это номер карты
        if len(number) == 16:
            hiding_card = '** **** '
            return title + number[:4] + ' ' + number[4:6] + hiding_card + number[-4:]
        # Если это номер счета
        else:
            hiding_account = '**'
            return title + hiding_account + number[-4:]

    def get_currency(self):
        """
        Возвращает сумму перевода и название валюты
        """
        return self.amount + ' ' + self.name_currency
