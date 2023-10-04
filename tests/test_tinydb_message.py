import pytest
import os
import json

from rul.tiny import TinyMessage

JSON_FILE = "test.json"


@pytest.fixture(scope="function", autouse=True)
def setup_teardown_fixture():
    if os.path.exists(JSON_FILE):
        os.remove(JSON_FILE)


def test_get_messages():
    message_groups = [
        [
            {"id": 1, "header": "header1", "body": "body1"},
            {"id": 2, "header": "header2", "body": "body2"},
            {"id": 3, "header": "header3", "body": "body3"},
        ],
        [
            {"id": 1, "header": "header1", "body": "body1"},
        ],
    ]

    tiny_message = TinyMessage(JSON_FILE)
    assert tiny_message.getMessages() == []
    del tiny_message

    for messages in message_groups:
        with open(JSON_FILE, "w") as fw:
            data = [f'"{i}":{json.dumps(m)}' for i, m in enumerate(messages)]
            text = '{"_default":{%s}}' % (",".join(data))
            fw.write(text)
        tiny_message = TinyMessage(JSON_FILE)
        assert tiny_message.getMessages() == messages


def test_post_messages():
    message_groups = [
        [
            {"header": "header1", "body": "body1"},
            {"header": "header2", "body": "body2"},
            {"header": "header3", "body": "body3"},
        ],
        [
            {"header": "header1", "body": "body1"},
        ],
    ]

    for messages in message_groups:
        if os.path.exists(JSON_FILE):
            os.remove(JSON_FILE)
        tiny_message = TinyMessage(JSON_FILE)
        messages_with_id = []
        for i, message in enumerate(messages):
            tiny_message.postMessage(message["header"], message["body"])
            message["id"] = i + 1
            messages_with_id.append(message)

        assert messages_with_id == tiny_message.getMessages()
        del tiny_message
