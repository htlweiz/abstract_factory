""" Concrete JsonMessage implementation

@author Emanuel Ableitner
"""

import json
import os
from typing import List

from .._message import AbstractMessage


class JsonMessage(AbstractMessage):
    def __init__(self, filename: str):
        self._jsonfile = filename

        # create file
        if not os.path.isfile(self._jsonfile):
            with open(self._jsonfile, "w+") as f:
                f.write("[]")

    def getMessages(self) -> List[object]:
        """Retrieve all Messages

        Returns:
            List[object]: list of message representative objects in form:
                          { "id": id, "header": header, "body": body }
        """
        with open(self._jsonfile, "r") as f:
            data = json.load(f)

        return data

    def postMessage(self, header: str, body: str) -> None:
        """Post new message

        Args:
            header (str): message header text
            body (str): message body text
        """
        data = self.getMessages()
        new_obj = {
            "id": len(data),
            "header": header,
            "body": body
        }
        data.append(new_obj)
        with open(self._jsonfile, "w") as f:
            json.dump(data, f)
