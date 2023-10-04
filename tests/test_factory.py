from rul._factory import TinyMessage, TinyMessageFactory


def test_factory():
    factory = TinyMessageFactory()
    message = factory.buildMessage()
    assert isinstance(message, TinyMessage)
