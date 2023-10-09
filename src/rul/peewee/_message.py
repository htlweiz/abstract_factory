""" Concrete PeeWee implementation of Message

@author Robert Ulmer
"""

from typing import List

from peewee import SqliteDatabase

from .._message import AbstractMessage
from ._model import OrmMessage


class PeeWeeMessage(AbstractMessage):
    """
    PeeWeeMessage
    """

    def __init__(self, db_file: str):
        """initialize Message and bind to db

        Args:
            db_file (str): sqlite db file
        """
        self._db = SqliteDatabase(db_file)
        OrmMessage.bind(self._db)
        self._db.connect()
        self._db.create_tables([OrmMessage])

    def get_messages(self) -> List[object]:
        """Retrieve all Message

        Returns:
            List[object]: list of message representative objects in form:
                          { "id": id, "header": header, "body": body }
        """
        return_value = []
        for message in OrmMessage.select():
            return_value.append(
                {"id": message.id, "header": message.header, "body": message.body}
            )
        return return_value

    def post_message(self, header, body):
        """Post new message

        Args:
            header (str): message header text
            body (str): message body text
        """
        message = OrmMessage()
        message.body = body
        message.header = header
        message.save()
