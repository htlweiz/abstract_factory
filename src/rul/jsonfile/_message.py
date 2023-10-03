""" Concrete JsonMessage implementation

@author Emanuel Ableitner
"""

from typing import List

import json
import os

from .._message import AbstractMessage

class JsonMessage(AbstractMessage):
    def __init__(self, filename: str):
        self._init = False
        self._jsonfile = filename

    def initialize(self) -> None:
        """create db file

        Args:
            db_name (str): Sqlite file to bind to.
        """
        if not os.path.isfile(self._jsonfile):
            with open(self._jsonfile, "w+") as f:
                f.write("[]")
        self._init = True

    def getMessages(self) -> List[object]:
        """Retrieve all Message

        Returns:
            List[object]: list of message representative objects in form:
                          { "id": id, "header": header, "body": body }
        """
        if not self._init:
            raise RuntimeError("Not initialized")
        
        with open(self._jsonfile, "r") as f:
            data = json.load(f)
        
        return data

    def postMessage(self, header: str, body: str) -> None:
        """Post new message

        Args:
            header (str): message header text
            body (str): message body text
        """
        if not self._init:
            raise RuntimeError("Not initialized")

        data = self.getMessages()
        new_obj = {
            "id": len(data),
            "header": header,
            "body": body
        }
        data.append(new_obj)
        with open(self._jsonfile, "w") as f:
            json.dump(data, f)
