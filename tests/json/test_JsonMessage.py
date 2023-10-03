from rul.json import JsonMessage
import os


def test_init():
    jsonMsg = JsonMessage("test.json")
    assert jsonMsg
    assert type(jsonMsg) == JsonMessage


def test_initialize():
    jsonMsg = JsonMessage("test.json")
    jsonMsg.initialize()
    assert os.path.exists("test.json")
    os.remove("test.json")
