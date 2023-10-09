""" In this module the factories are defined

@author Robert Ulmer | Lukas Lackner
"""
from abc import ABC, abstractmethod

from rul.peewee import PeeWeeMessage
from rul.sqlalchemy import AlchemyMessage
from rul.json import JSONMessage


class AbstractMessageFactory(ABC):
    """
    Abstract Factory
    """

    @abstractmethod
    def buildMessage(self):
        """factory interface"""
        pass


class AlchemyMessageFactory(AbstractMessageFactory):
    def buildMessage(self) -> AlchemyMessage:
        """builds and returns a SQLAlchemy Message implementation

        Returns:
            AlchemyMessage: already initialized AlchemyMessage pointing to
                            'alchemy.sqlite' db.
        """
        message = AlchemyMessage()
        message.initialize("alchemy.sqlite")
        return message


class PeeWeeMessageFactory(AbstractMessageFactory):
    def buildMessage(self) -> PeeWeeMessage:
        """builds and return a PeeWee Message implementation

        Returns:
            PeeWeeMessage: already initialized PeeWeeMessage pointing to
            'peewee.sqlite' db.
        """
        message = PeeWeeMessage("peewee.sqlite")
        return message


class JSONMessageFactory(AbstractMessageFactory):
    def buildMessage(self) -> JSONMessage:
        """builds and return a JSON Message implementation

        Returns:
            JSONMessage: already initialized JSON pointing to
            'json.json' file.
        """
        message = JSONMessage("json.json")
        return message
