""" Author: Kevin Schneidhofer
   Course: 5AHIT-INSY
   History: 20231028 00:08 Kevin Schneidhofer - Created
            20231028 01:30 Kevin Schneidhofer - Added tests for PeeWeeMessage
"""


import os

import peewee
import pytest

from rul.peewee import PeeWeeMessage
from src.rul.peewee._model import OrmMessage

absolute_path_name = os.getcwd()
relative_test_db = "\\src\\test_data\\test_peeweeMessage.sqlite"
test_db = absolute_path_name + relative_test_db


@pytest.fixture
def peewee_message():
    db = peewee.SqliteDatabase(test_db)

    OrmMessage.bind(db)

    db.connect()
    db.create_tables([OrmMessage])

    peeWeeMessage = PeeWeeMessage(test_db)
    return peeWeeMessage


def test_get_messages(peewee_message):
    messages = peewee_message.getMessages()
    assert isinstance(messages, list)
    for message in messages:
        assert isinstance(message, dict)
        assert "id" in message
        assert "header" in message
        assert "body" in message


def test_post_message(peewee_message):
    header = "Test Header"
    body = "Test Body"
    peewee_message.postMessage(header, body)

    messages = peewee_message.getMessages()
    assert any(message["header"] == header and
               message["body"] == body for message in messages)


if __name__ == '__main__':
    pytest.main()
