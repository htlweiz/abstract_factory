import json
import os

from rul import JsonMessageFactory
from rul.jsonfile import JsonMessage
from tests.conftest import TEST_JSON_FILE


def test_import():
    assert JsonMessage
    assert JsonMessageFactory


def test_create(json_message_factory: JsonMessageFactory):
    assert isinstance(json_message_factory, JsonMessageFactory)
    assert json_message_factory._jsonfile_path == TEST_JSON_FILE

    json_message = json_message_factory.buildMessage()

    assert isinstance(json_message, JsonMessage)
    assert json_message._jsonfile == TEST_JSON_FILE
    assert os.path.isfile(TEST_JSON_FILE)
    with open(TEST_JSON_FILE, "r") as f:
        assert f.read()


def test_get(json_message: JsonMessage):
    test_data = [{
        "id": 0,
        "header": "test subject 1",
        "body": "this is the test body"
    }, {
        "id": 1,
        "header": "test subject 2",
        "body": "this is another test body"
    }]

    with open(TEST_JSON_FILE, "w+") as f:
        json.dump(test_data, f)

    read_data = json_message.getMessages()

    assert isinstance(read_data, list)
    for i, data in enumerate(test_data):
        assert data == read_data[i]


def test_post(json_message: JsonMessage):
    test_data = [{
        "id": 0,
        "header": "test subject 1",
        "body": "this is the test body"
    }, {
        "id": 1,
        "header": "test subject 2",
        "body": "this is another test body"
    }]

    for item in test_data:
        json_message.postMessage(item["header"], item["body"])

    with open(TEST_JSON_FILE, "r") as f:
        read_data = json.load(f)

    assert isinstance(read_data, list)
    for i, data in enumerate(test_data):
        assert data == read_data[i]
