""" Concrete JSON implementation

@author Lukas Lackner
"""

from os.path import isfile
from typing import List

import json

from .._message import AbstractMessage

class JSONMessage(AbstractMessage):
    def __init__(self, file_path: str):
        """Initialize system and set file_path

        Args:
            file_path (str): file path to json file, will be created if it does not exist yet.
        """
        self.file_path = file_path

    def getMessages(self) -> List[object]:
        """Retrieve all Messages

        Returns:
            List[object]: list of message representative objects in form:
                          { "id": id, "header": header, "body": body }
        """

        if not isfile(self.file_path):
            return {}
        with open(self.file_path, "r") as f:
            messages = json.load(f)
        if isinstance(messages, dict):
            return [messages]
        return messages

    def postMessage(self, header: str, body: str) -> None:
        """Post new message

        Args:
            header (str): message header text
            body (str): message body text
        """

        id = len(self.getMessages()) + 1
        message = {
            "id": id,
            "header": header,
            "body": body,
        }
        if isfile(self.file_path):
            messages = self.getMessages()
            if type(messages) is dict:
                messages = [messages]
            messages.append(message)
        else:
            messages = message

        with open(self.file_path, "w") as f:
            json.dump(messages, f)
