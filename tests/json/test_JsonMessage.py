from rul.json import JsonMessage


def test_init():
    jsonMsg = JsonMessage("test.json")
    assert jsonMsg
    assert type(jsonMsg) == JsonMessage
