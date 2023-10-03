"""
Testing the SqlAlchemy Module.
"""

import os
import pytest
from rul.sqlalchemy import AlchemyMessage


# Path to SQLite database file
TEST_DB_FILE = "test_messages.db"


@pytest.fixture
def alchemy_message():
    """
    Fixture for the AlchemyMessage instance with the test SQLite database.
    """
    message = AlchemyMessage()
    yield message
    # Cleanup the test SQLite database after the test
    message._engine.dispose()
    if os.path.exists(TEST_DB_FILE):
        os.remove(TEST_DB_FILE)


def test_initialize(alchemy_message):
    """
    Test initialization of AlchemyMessage and binding to a database.
    """
    assert not alchemy_message._init

    # Initialize the AlchemyMessage
    alchemy_message.initialize(TEST_DB_FILE)

    # Check if initialized
    assert alchemy_message._init

    # Check if the database file exists
    assert os.path.exists(TEST_DB_FILE)


def test_get_messages(alchemy_message):
    """
    Test retrieving messages from the database.
    """
    # Initialize and add test messages
    alchemy_message.initialize(TEST_DB_FILE)
    alchemy_message.postMessage("Test Header 1", "Test Body 1")
    alchemy_message.postMessage("Test Header 2", "Test Body 2")

    # Retrieve messages
    messages = alchemy_message.getMessages()

    # Check the number of retrieved messages
    assert len(messages) == 2

    # Check the content of the retrieved messages
    assert messages[0]["header"] == "Test Header 1"
    assert messages[0]["body"] == "Test Body 1"
    assert messages[1]["header"] == "Test Header 2"
    assert messages[1]["body"] == "Test Body 2"


def test_post_message(alchemy_message):
    """
    Test posting a new message to the database.
    """
    # Initialize and post a message
    alchemy_message.initialize(TEST_DB_FILE)
    alchemy_message.postMessage("Test Header", "Test Body")

    # Retrieve messages and check the number of messages
    messages = alchemy_message.getMessages()
    assert len(messages) == 1

    # Check the content of the posted message
    assert messages[0]["header"] == "Test Header"
    assert messages[0]["body"] == "Test Body"
