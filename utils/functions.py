import json
from utils import classes
import os

path_ = os.path.abspath('operations.json')
DATA = json.load(open(os.path.join(path_),  encoding='utf-8'))


def get_last_transactions():
    """
    Возвращает список из 5 последних выполненных операций, начиная с последней операции
    """
    # Создаем пустой список для всех выполненных транзакций
    necessary_date = []
    # Проходимся циклом по списку всех транзакций начиная с конца
    for transaction in reversed(DATA):
        # Если ключа 'state' нету в словаре (элементе списка), то пропускаем итерацию
        if 'state' not in transaction.keys():
            continue
        # Если ключ 'state' равен значению 'EXECUTED', то добавляем этот элемент в список выполненных операций
        if transaction['state'] == 'EXECUTED':
            necessary_date.append(transaction)
    # Возвращаем последние 5 выполненных операций
    return necessary_date[:5]


def transaction_in_class():
    """
    Принимает список транзакций и возвращает список экземпляров класса Transaction
    """
    # Создаем пустой список для будущих экземпляров
    list_ = get_last_transactions()
    list_of_classes = []

    # Проходимся циклом по последним транзакцим, задаем аргументы для экземпляра
    for element in list_:
        id_ = element['id']
        state = element['state']
        date = element['date']
        amount = element['operationAmount']['amount']
        name_currency = element['operationAmount']['currency']['name']
        code_currency = element['operationAmount']['currency']['code']
        description = element['description']
        # Если есть счет отправителя
        if 'from' in element.keys():
            sender = element['from']
        else:
            sender = ''
        recipient = element['to']

        # Инициализируем экземпляр
        transaction = classes.Transaction(id_, state, date, amount, name_currency, code_currency, description, sender,
                                          recipient)
        # Добавляем его в список
        list_of_classes.append(transaction)
    # Выводим список экземпляров
    return list_of_classes


def main():
    for transaction in transaction_in_class():
        print(transaction)
