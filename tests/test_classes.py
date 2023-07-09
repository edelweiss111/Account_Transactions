import pytest
from utils.classes import Transaction

DATA_1 = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
        "amount": "31957.58",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
}

DATA_2 = {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
        "amount": "9824.07",
        "currency": {
            "name": "USD",
            "code": "USD"
        }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
}

DATA_3 = {
    "id": 587085106,
    "state": "EXECUTED",
    "date": "2018-03-23T10:45:06.972075",
    "operationAmount": {
        "amount": "48223.05",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Открытие вклада",
    "to": "Счет 41421565395219882431"
}

DATA_4 = {
    "id": 895315941,
    "state": "EXECUTED",
    "date": "2018-08-19T04:27:37.904916",
    "operationAmount": {
        "amount": "56883.54",
        "currency": {
            "name": "USD",
            "code": "USD"
        }
    },
    "description": "Перевод с карты на карту",
    "from": "Visa Classic 6831982476737658",
    "to": "Visa Platinum 8990922113665229"
}


@pytest.fixture
def data():
    """
    Фикстура для тестовых данных
    """
    transaction_1 = Transaction(DATA_1['id'], DATA_1['state'], DATA_1['date'], DATA_1['operationAmount']['amount'],
                                DATA_1['operationAmount']['currency']['name'],
                                DATA_1['operationAmount']['currency']['code'],
                                DATA_1['description'], DATA_1['from'], DATA_1['to'])

    transaction_2 = Transaction(DATA_2['id'], DATA_2['state'], DATA_2['date'], DATA_2['operationAmount']['amount'],
                                DATA_2['operationAmount']['currency']['name'],
                                DATA_2['operationAmount']['currency']['code'],
                                DATA_2['description'], DATA_2['from'], DATA_2['to'])

    transaction_3 = Transaction(DATA_3['id'], DATA_3['state'], DATA_3['date'], DATA_3['operationAmount']['amount'],
                                DATA_3['operationAmount']['currency']['name'],
                                DATA_3['operationAmount']['currency']['code'],
                                DATA_3['description'], '', DATA_3['to'])

    transaction_4 = Transaction(DATA_4['id'], DATA_4['state'], DATA_4['date'], DATA_4['operationAmount']['amount'],
                                DATA_4['operationAmount']['currency']['name'],
                                DATA_4['operationAmount']['currency']['code'],
                                DATA_4['description'], DATA_4['from'], DATA_4['to'])

    return transaction_1, transaction_2, transaction_3, transaction_4


def test_get_date(data):
    """
    Тест метода, который возвращает дату
    """
    assert data[0].get_date() == '26.08.2019 '


def test_hiding_sender(data):
    """
    Тест метода, который скрывает номер карты/счета отправителя
    """
    assert data[0].hiding_sender() == 'Maestro 1596 83** **** 5199 -> '
    assert data[1].hiding_sender() == 'Счет **6952 -> '
    assert data[2].hiding_sender() == '-> '


def test_hiding_recipient(data):
    """
    Тест метода, который скрывает номер карты/счета получателя
    """
    assert data[0].hiding_recipient() == "Счет **9589"
    assert data[3].hiding_recipient() == "Visa Platinum 8990 92** **** 5229"


def test_get_currency(data):
    """
    Тест метода, который возвращает сумму перевода и валюту
    """
    assert data[0].get_currency() == "31957.58 руб."
