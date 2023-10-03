""" Concrete AlchemyMessage implementation

@author Robert Ulmer
"""

from typing import List
from pymongo import MongoClient
from .._message import AbstractMessage


class MongoMessage(AbstractMessage):
    def __init__(self):
        self._init = False

    def initialize(self, db_name: str) -> None:
        """Initialize system and bind to db

        Args:
            db_name (str): Mongodb name.
        """
        self.server = MongoClient('localhost', 27017)
        self.db = self.server[db_name]
        self.collection = self.db['messages']
        self._init = True

    def getMessages(self) -> List[dict]:
        """Retrieve all Message

        Returns:
            List[object]: list of message representative objects in form:
                          { "id": id, "header": header, "body": body }
        """
        if not self._init:
            raise RuntimeError("Not initialized")

        messages = self.collection.find()
        data = []
        for msg in messages:
            data.append({
                "id": str(msg["_id"]),
                "header": msg["header"],
                "body": msg["body"]
            })
        return data

    def postMessage(self, header: str, body: str) -> None:
        """Post new message

        Args:
            header (str): message header text
            body (str): message body text
        """
        if not self._init:
            raise RuntimeError("Not initialized")

        message = {
            "header": header,
            "body": body
        }

        self.collection.insert_one(message)
