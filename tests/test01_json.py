"""
Testing the Json Module.
"""

import os
import json
import pytest
from rul.json import JsonMessage

# Path to Test-JSON-File
TEST_JSON_FILE = "test_messages.json"


@pytest.fixture
def json_message():
    """
    Fixture for the JsonMessage instance with the test JSON file.
    """

    json_message = JsonMessage(TEST_JSON_FILE)
    yield json_message


def test_load_messages_existing_file(json_message):
    """
    Test loading messages from an existing JSON file.
    """
    test_data = [{"id": 1, "header": "Test Header", "body": "Test Body"}]

    # Set messages
    json_message.messages = test_data

    # Create JSON file with test data
    with open(TEST_JSON_FILE, "w", encoding='utf-8') as file:
        json.dump(test_data, file)

    # Load messages and verify
    messages = json_message._load_messages()
    # Messages should be updated with data loaded from the JSON file
    assert json_message.messages == test_data
    # The returned message list should also match the data loaded from the JSON file
    assert messages == test_data


def test_save_messages(json_message):
    """
    Test saving messages to a JSON file.
    """

    # Test data
    test_data = [{"id": 1, "header": "Test Header", "body": "Test Body"}]

    # Set messages
    json_message.messages = test_data

    # Save messages
    json_message._save_messages()

    # Check JSON file
    with open(TEST_JSON_FILE, "r") as file:
        saved_data = json.load(file)
        # The saved data should be identical to the test data
        assert saved_data == test_data


def test_get_messages(json_message):
    """
    Test getting messages.
    """
    if os.path.exists(TEST_JSON_FILE):
        os.remove(TEST_JSON_FILE)
    # Test data
    test_data = [{"id": 1, "header": "Test Header", "body": "Test Body"}]

    # Set messages
    json_message.messages = test_data

    # Get messages and verify
    retrieved_messages = json_message.getMessages()
    assert retrieved_messages == test_data


def test_post_message(json_message):
    """
    Test posting a message.
    """
    if os.path.exists(TEST_JSON_FILE):
        os.remove(TEST_JSON_FILE)
    assert json_message.messages == []

    # Post a message
    json_message.postMessage("Test Header", "Test Body")

    # Check messages
    assert len(json_message.messages) == 1
    assert json_message.messages[0]["header"] == "Test Header"
    assert json_message.messages[0]["body"] == "Test Body"
