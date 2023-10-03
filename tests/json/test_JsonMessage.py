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


def test_getMessage():
    jsonMsg = JsonMessage("test.json")
    jsonMsg.initialize()
    with open("test.json", "w") as writefile:
        writefile.write("[{\"id\": 0, \"header\": \"Head\", \"body\": \"Body\"}]")
    msg = jsonMsg.getMessages()
    assert msg == [{"id": 0, "header": "Head", "body": "Body"}]
    os.remove("test.json")


def test_postMessage():
    jsonMsg = JsonMessage("test.json")
    jsonMsg.initialize()
    jsonMsg.postMessage("Head", "Body")
    with open("test.json", "r") as outfile:
        content = outfile.read()
    assert content == "{\"id\": 0, \"header\": \"Head\", \"body\": \"Body\"}"
    os.remove("test.json")
