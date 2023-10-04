"""Concrete TinyDB implementation of Message

@author Matthias Derler
"""
from typing import List

from tinydb import TinyDB

from .._message import AbstractMessage


class TinyMessage(AbstractMessage):
    def __init__(self, json_file: str) -> None:
        self._db = TinyDB(json_file)

    def getMessages(self) -> List[object]:
        """Retrieve all Message

        Returns:
            List[object]: list of message representative objects in form:
                          { "id": id, "header": header, "body": body }
        """

        return self._db.all()

    def postMessage(self, header: str, body: str) -> None:
        """Post new message

        Args:
            header (str): message header text
            body (str): message body text
        """

        message_id = self._db.insert({"header": header, "body": body})
        self._db.update({"id": message_id}, doc_ids=[message_id])
