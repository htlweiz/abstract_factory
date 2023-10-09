""" In this module the factories are defined

@author Robert Ulmer
"""
from abc import ABC, abstractmethod

from rul.peewee import PeeWeeMessage
from rul.sqlalchemy import AlchemyMessage
from rul.json import JsonMessage


class AbstractMessageFactory(ABC):
    """
    Abstract Factory
    """

    @abstractmethod
    def build_message(self):
        """factory interface"""



class AlchemyMessageFactory(AbstractMessageFactory):
    """
    AlchemyMessage Factory
    """

    def build_message(self) -> AlchemyMessage:
        """builds and returns a SQLAlchemy Message implementation

        Returns:
            AlchemyMessage: already initialized AlchemyMessage pointing to
                            'alchemy.sqlite' db.
        """
        message = AlchemyMessage()
        message.initialize("alchemy.sqlite")
        return message


class PeeWeeMessageFactory(AbstractMessageFactory):
    """
    PeeWeeMessageFactory
    """

    def build_message(self) -> PeeWeeMessage:
        """builds and return a PeeWee Message implementation

        Returns:
            PeeWeeMessage: already initialized PeeWeeMessage pointing to
            'peewee.sqlite' db.
        """
        message = PeeWeeMessage("peewee.sqlite")
        return message


class JsonMessageFactory(AbstractMessageFactory):
    """
    JsonMessageFactory
    """

    def build_message(self) -> JsonMessage:
        """builds and return a Json Message implementation

        Returns:
            JsonMessage: already initialized JsonMessage pointing to
            'data.json'.
        """
        message = JsonMessage("data.json")
        return message
