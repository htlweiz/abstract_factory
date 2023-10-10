import json
import os
import pytest
from rul.json.json_message import JSONMessage


TEST_JSON_FILE = "test_messages.json"

@pytest.fixture
def json_message():
    return JSONMessage(TEST_JSON_FILE)

def test_post_message(json_message):
    json_message.postMessage("Test Header", "Test Body")
    messages = json_message.getMessages()
    assert len(messages) == 1
    assert messages[0]["header"] == "Test Header"
    assert messages[0]["body"] == "Test Body"

def test_get_messages(json_message):
    json_message.messages = [{"id": 1, "header": "Header 1", "body": "Body 1"}]
    messages = json_message.getMessages()
    assert len(messages) == 1
    assert messages[0]["header"] == "Header 1"
    assert messages[0]["body"] == "Body 1"

def teardown():
    os.remove(TEST_JSON_FILE)

if __name__ == "__main__":
    pytest.main()
