"""
JSON implementation of Message
"""

from typing import List

import os
import json
from .._message import AbstractMessage
from ._model import JSONModel


class JSONMessage(AbstractMessage):
    def __init__(self, db_file: str):
        """initialize Message and bind to db

        Args:
            db_file (str): json file
        """
        self._db = db_file

    def getMessages(self) -> List[object]:
        """Retrieve all Message

        Returns:
            List[object]: list of message representative objects in form:
                          { "id": id, "header": header, "body": body }
        """

        if os.path.exists(self._db):
            return_value = []
            file = open(self._db)
            data = json.load(file)
            for line in data:
                return_value.append(
                    {"id": line["id"], "header": line["header"], "body": line["body"]}
                )
        else:
            return []
        return return_value

    def postMessage(self, header: str, body: str) -> None:
        """Post new message

        Args:
            header (str): message header text
            body (str): message body text
        """

        with open(self._db, 'r') as file:
            file_data = json.load(file)

        _id = self.getLastId()

        message = JSONModel(_id + 1, header, body)
        file_data.append(message.ToDict())

        with open(self._db, 'w') as file:
            json.dump(file_data, file, indent=4)

    def getLastId(self) -> int:
        """Get the id of the last input and return a new one, raised by one.
        """

        current_file = self.getMessages()
        _id = int(current_file[-1]["id"])

        return _id
