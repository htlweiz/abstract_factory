""" Concrete json implementation of Message

@author Philipp Lorber
"""

import os
import json
from typing import List

from .._message import AbstractMessage

class JsonMessage(AbstractMessage):
    """
    JsonMessage
    """
    def __init__(self, name: str) -> None:
        self.file = name

        if not os.path.isfile(self.file):
            with open(self.file, "w") as outfile:
                outfile.write("{}")

    def get_messages(self) -> List[object]:
        """Retrieve all Message

        Returns:
            List[object]: list of message representative objects in form:
                          { "id": id, "header": header, "body": body }
        """
        _f = open(self.file)
        data = json.load(_f)

        return data

    def post_message(self, header: str, body: str) -> None:
        """Post new message

        Args:
            header (str): message header text
            body (str): message body text
        """
        data = self.get_messages()
        message = {
            "id": len(data),
            "header": header,
            "body": body
        }
        data.append(message)
        with open(self.file, "w") as outfile:
            json.dump(data, outfile)
