""" Concrete AlchemyMessage implementation

@author Robert Ulmer
"""

from typing import List

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from .._message import AbstractMessage
from ._model import Base, Message


class AlchemyMessage(AbstractMessage):
    """
    AlchemyMessage
    """

    def __init__(self):
        self._init = False
        self._engine = None

    def initialize(self, db_name: str) -> None:
        """Initialize system and bind to db

        Args:
            db_name (str): Sqlite file to bind to.
        """
        self._engine = create_engine("sqlite:///%s" % db_name, echo=False)
        Base.metadata.create_all(self._engine)
        self._init = True

    def get_messages(self) -> List[object]:
        """Retrieve all Message

        Returns:
            List[object]: list of message representative objects in form:
                          { "id": id, "header": header, "body": body }
        """
        if not self._init:
            raise RuntimeError("Not initialized")

        session = Session(self._engine)
        return_values = []
        statement = select(Message)
        for message in session.scalars(statement):
            return_values.append(
                {
                    "id": message.message_id,
                    "header": message.header_text,
                    "body": message.body_text,
                }
            )
        return return_values

    def post_message(self, header: str, body: str) -> None:
        """Post new message

        Args:
            header (str): message header text
            body (str): message body text
        """
        if not self._init:
            raise RuntimeError("Not initialized")

        session = Session(self._engine)
        message = Message()
        message.header_text = header
        message.body_text = body
        session.add(message)
        session.commit()
