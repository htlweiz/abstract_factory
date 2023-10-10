import json
import os

from typing import List

from .._message import AbstractMessage

class JsonMessage(AbstractMessage):
    def __init__(self, db_file: str):
        self._init = False
        self.jsonfile = db_file


    def initialize(self) -> None:
        """Initialize system and bind to db

        Args:
            jsonfile (str): JSON file to bind to.
        """
        if not os.path.isfile(self.jsonfile):
            f = open(self.jsonfile, "w+")
        self._init = True

    def getMessages(self) -> List[object]:
        """Retrieve all Message

        Returns:
            List[object]: list of message representative objects in form:
                          { "id": id, "header": header, "body": body }
        """
        data: dict = {}
        with open(self.jsonfile, "r") as jsonfile:
            data = json.load(jsonfile)
        
        return data

    def postMessage(self, header: str, body: str) -> None:
        """Post new message

        Args:
            header (str): message header text
            body (str): message body text
        """
        if not self._init:
            raise RuntimeError("Not initialized")

        data: dict = self.getMessages()
        new_id = len(data) + 1
        new_message = {"id": new_id, "header": header, "body": body}
        data[new_id] = new_message
        with open(self.jsonfile, "w") as jsonfile:
            json.dump(data, jsonfile, indent=2)
