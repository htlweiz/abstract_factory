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
        messages = list(map(lambda x: {
            "id": x.doc_id,
            "header": x["header"],
            "body": x["body"]},
            self._db.all()))

        return messages

    def postMessage(self, header: str, body: str) -> None:
        """Post new message

        Args:
            header (str): message header text
            body (str): message body text
        """

        self._db.insert({"header": header, "body": body})
