from rul.json import JsonMessage
import os


def test_init():
    jsonMsg = JsonMessage("test.json")
    assert jsonMsg
    assert type(jsonMsg) == JsonMessage
    os.remove("test.json")


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

    jsonMsg.postMessage("Head1", "Body1")
    with open("test.json", "r") as outfile:
        content = outfile.read()
    assert content == "[{\"id\": 0, \"header\": \"Head1\", \"body\": \"Body1\"}]"

    jsonMsg.postMessage("Head2", "Body2")
    with open("test.json", "r") as outfile:
        content = outfile.read()
    assert content == "[{\"id\": 0, \"header\": \"Head1\", \"body\": \"Body1\"}, \
{\"id\": 1, \"header\": \"Head2\", \"body\": \"Body2\"}]"

    os.remove("test.json")


def test__new_id_first():
    jsonMsg = JsonMessage("test.json")
    jsonMsg.initialize()

    assert jsonMsg._new_id() == 0
    os.remove("test.json")


def test_new_id():
    jsonMsg = JsonMessage("test.json")
    jsonMsg.initialize()

    with open("test.json", "w") as writefile:
        writefile.write("[{\"id\": 0, \"header\": \"Head\", \"body\": \"Body\"}]")

    assert jsonMsg._new_id() == 1
    os.remove("test.json")
