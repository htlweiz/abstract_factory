"""
Test the Factory Module.
"""

import pytest

from rul import AlchemyMessageFactory, PeeWeeMessageFactory, JsonMessageFactory
from rul.peewee import PeeWeeMessage
from rul.sqlalchemy import AlchemyMessage
from rul.json import JsonMessage


def test_alchemy_message_factory_build_message():
    """
    Test function to verify AlchemyMessageFactory buildMessage method.
    """

    # Create an instance of AlchemyMessageFactory
    factory = AlchemyMessageFactory()

    # Build a message using the factory
    message = factory.buildMessage()

    # Check if the message is an instance of AlchemyMessage
    assert isinstance(message, AlchemyMessage)


def test_peewee_message_factory_build_message():
    """
    Test function to verify PeeWeeMessageFactory buildMessage method.
    """

    # Create an instance of PeeWeeMessageFactory
    factory = PeeWeeMessageFactory()

    # Build a message using the factory
    message = factory.buildMessage()

    # Check if the message is an instance of PeeWeeMessage
    assert isinstance(message, PeeWeeMessage)


def test_json_message_factory_build_message():
    """
    Test function to verify JsonMessageFactory buildMessage method.
    """

    # Create an instance of JsonMessageFactory
    factory = JsonMessageFactory()

    # Build a message using the factory
    message = factory.buildMessage()

    # Check if the message is an instance of JsonMessage
    assert isinstance(message, JsonMessage)
