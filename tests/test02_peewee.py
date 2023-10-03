"""
Testing the PeeWee Module.
"""

import os
import pytest
from rul.peewee import _message


# Path to SQLite database file
TEST_DB_FILE = 'test_peewee.sqlite'


@pytest.fixture
def setup_peewee_db():
    """
    Fixture to set up the PeeWee database for testing.

    This fixture creates a test database and tables, provides the fixture object to the tests,
    and deletes the test database file after tests.

    Yields:
        PeeWeeMessage: A PeeWeeMessage instance for testing.
    """
    peewee_message_instance = _message.PeeWeeMessage(TEST_DB_FILE)
    yield peewee_message_instance
    os.remove(TEST_DB_FILE)


def test_get_messages(setup_peewee_db):
    """
    Test for retrieving messages from the PeeWee database.

    Args:
        setup_peewee_db (fixture): Fixture to set up the PeeWee database for testing.
    """
    # Ensure the database is set up and empty
    assert setup_peewee_db.getMessages() == []

    # Insert a test message
    test_header = 'Test Header'
    test_body = 'Test Body'
    setup_peewee_db.postMessage(test_header, test_body)

    # Retrieve messages and check the content
    messages = setup_peewee_db.getMessages()
    assert len(messages) == 1
    assert messages[0]['header'] == test_header
    assert messages[0]['body'] == test_body


def test_post_message(setup_peewee_db):
    """
    Test for posting a new message to the PeeWee database.

    Args:
        setup_peewee_db (fixture): Fixture to set up the PeeWee database for testing.
    """
    # Ensure the database is set up and empty
    assert setup_peewee_db.getMessages() == []

    # Post a new message
    test_header = 'Test Header'
    test_body = 'Test Body'
    setup_peewee_db.postMessage(test_header, test_body)

    # Check if the message was inserted correctly
    messages = setup_peewee_db.getMessages()
    assert len(messages) == 1
    assert messages[0]['header'] == test_header
    assert messages[0]['body'] == test_body
