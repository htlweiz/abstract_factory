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

    def getMessages(self) -> List[object]:
        """Retrieve all Message

        Returns:
            List[object]: list of message representative objects in form:
                          { "id": id, "header": header, "body": body }
        """
        with open(self.json_file, "r") as openfile:
            openfile.seek(0)
            try:
                messages = json.load(openfile)
            except json.JSONDecodeError as e:
                print(e)
                return []
        return messages

    def postMessage(self, header: str, body: str) -> None:
        """Post new message

        Args:
            header (str): message header text
            body (str): message body text
        """

        old_msg = self.getMessages()

        new_msg = {
            "id": self._new_id(),
            "header": header,
            "body": body
        }

        old_msg.append(new_msg)

        with open(self.json_file, "w") as writefile:
            writefile.write(str(old_msg).replace("'", "\""))

    def _new_id(self):
        msg = self.getMessages()
        if len(msg) <= 0:
            return 0
        return msg[-1]["id"] + 1
