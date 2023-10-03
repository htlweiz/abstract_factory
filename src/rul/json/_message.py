import json
from typing import List

from .._message import AbstractMessage


class JsonMessage(AbstractMessage):
    def __init__(self, json_file: str) -> None:
        """initialize Message and bind to db

        Args:
            json_file (str): json file
        """
        self.json_file = json_file

    def initialize(self) -> None:
        """Create Json File if not exists.
        """
        with open(self.json_file, "w"):
            pass

    def getMessages(self) -> List[object]:
        """Retrieve all Message

        Returns:
            List[object]: list of message representative objects in form:
                          { "id": id, "header": header, "body": body }
        """
        with open(self.json_file, "r") as openfile:
            messages = json.load(openfile)

        return messages

    def postMessage(self, header: str, body: str) -> None:
        """Post new message

        Args:
            header (str): message header text
            body (str): message body text
        """

        new_msg = {
            "id": 0,
            "header": header,
            "body": body
        }

        json_dump = json.dumps(new_msg)

        with open(self.json_file, "w") as writefile:
            writefile.write(json_dump)
