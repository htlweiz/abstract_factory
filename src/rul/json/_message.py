""" Concrete AlchemyMessage implementation

@author Robert Ulmer
"""

from typing import List
import json
from .._message import AbstractMessage


class JsonMessage(AbstractMessage):
    def __init__(self):
        self._init = False

    def initialize(self, name: str) -> None:
        """Initialize system and bind to db

        Args:
            name (str): file name.
        """
        self.file_name = name
        self._init = True

    def getMessages(self) -> List[dict]:
        """Retrieve all Message

        Returns:
            List[dict]: dictionary of message representative objects in form:
                          { "id": id, "header": header, "body": body }
        """
        if not self._init:
            raise RuntimeError("Not initialized")

        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
        except (FileNotFoundError):
            data = []

        return data

    def postMessage(self, header: str, body: str) -> None:
        """Post new message

        Args:
            header (str): message header text
            body (str): message body text
        """
        if not self._init:
            raise RuntimeError("Not initialized")

        messages = self.getMessages()

        if messages:
            _id = messages[0]['id']
            for message in messages:
                _id = max(_id, message['id'])
            _id += 1
        else:
            _id = 1

        message = {
            "id": _id,
            "header": header,
            "body": body
        }

        messages.append(message)
        with open(self.file_name, 'w') as file:
            json.dump(messages, file)
