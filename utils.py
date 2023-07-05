import json

DATA = json.load(open('operations.json'))


def get_last_transactions():
    """
    Возвращает список из 5 последних выполненных операций
    """
    necessary_date = []

    for transaction in DATA:
        if 'state' not in transaction.keys():
            continue
        if transaction['state'] == 'EXECUTED':
            necessary_date.append(transaction)

    return necessary_date[-5:]
