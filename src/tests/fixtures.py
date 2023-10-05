import os

import pytest

from rul import JsonMessageFactory

TEST_JSON_FILE = "test.json"


@pytest.fixture(scope="function")
def json_message_factory():
    factory = JsonMessageFactory()
    factory._jsonfile_path = TEST_JSON_FILE

    yield factory

    # remove old test file
    if os.path.isfile(TEST_JSON_FILE):
        os.remove(TEST_JSON_FILE)


@pytest.fixture(scope="function")
def json_message():
    factory = JsonMessageFactory()
    factory._jsonfile_path = TEST_JSON_FILE
    message = factory.buildMessage()

    yield message

    # remove old test file
    if os.path.isfile(TEST_JSON_FILE):
        os.remove(TEST_JSON_FILE)
