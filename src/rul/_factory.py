""" In this module the factories are defined

@author Robert Ulmer
"""
from abc import ABC, abstractmethod

from rul.peewee import PeeWeeMessage
from rul.sqlalchemy import AlchemyMessage
from rul.json import *


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

class JsonMessageFactory(AbstractMessageFactory):
    def buildMessage(self) -> JsonMessage:
        message = JsonMessage("message.json")
        return message