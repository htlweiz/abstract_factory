""" Author: Kevin Schneidhofer
   Course: 5AHIT-INSY
   History: 20231028 00:08 Kevin Schneidhofer - Created
            20231028 00:45 Kevin Schneidhofer - Added tests for AlchemyMessage
"""


import os

import pytest

from rul.sqlalchemy import AlchemyMessage

absolute_path_name = os.getcwd()
relative_test_db = "\\src\\test_data\\test_alchemyMessage.sqlite"
test_db = absolute_path_name + relative_test_db


@pytest.fixture
def alchemy_message():
    alchemy_message = AlchemyMessage()
    alchemy_message.initialize(test_db)
    return alchemy_message


def test_initialize(alchemy_message):
    assert alchemy_message._init is True


def test_get_messages(alchemy_message):
    messages = alchemy_message.getMessages()
    assert isinstance(messages, list)
    for message in messages:
        assert isinstance(message, dict)
        assert "id" in message
        assert "header" in message
        assert "body" in message


def test_post_message(alchemy_message):
    header = "Test Header"
    body = "Test Body"
    alchemy_message.postMessage(header, body)

    messages = alchemy_message.getMessages()
    assert any(message["header"] == header and
               message["body"] == body for message in messages)


if __name__ == '__main__':
    pytest.main()
