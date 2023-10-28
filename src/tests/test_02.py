""" Author: Kevin Schneidhofer
   Course: 5AHIT-INSY
   History: 20231028 00:08 Kevin Schneidhofer - Created
            20231028 02:13 Kevin Schneidhofer - Added tests for JSONMessage
"""


import os

import pytest

from rul.json import JSONMessage

absolute_path_name = os.getcwd()
relative_test_db = "\\src\\test_data\\test_jsonMessage.json"
test_db = absolute_path_name + relative_test_db


@pytest.fixture
def json_message():
    json_message = JSONMessage(test_db)
    return json_message


@pytest.fixture(scope="session", autouse=True)
def teardown_fixture():
    open(test_db, 'w')


def test_post_message_and_get_messages(json_message):
    header = "Test Header"
    body = "Test Body"
    json_message.postMessage(header, body)
    messages = json_message.getMessages()
    assert isinstance(messages, list)
    assert len(messages) == 1
    assert messages[0]["header"] == header
    assert messages[0]["body"] == body


def test_get_messages(json_message):
    header = "Test Header"
    body = "Test Body"
    messages = json_message.getMessages()
    assert isinstance(messages, list)
    assert len(messages) == 1
    assert messages[0]["header"] == header
    assert messages[0]["body"] == body


if __name__ == '__main__':
    pytest.main()
