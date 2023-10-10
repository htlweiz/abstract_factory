from rul.main import PeeWeeMessageFactory, AlchemyMessageFactory


def test_get_messages():
    for factory in [PeeWeeMessageFactory, AlchemyMessageFactory]:
        message = factory().buildMessage()
        messages = message.getMessages()
        assert isinstance(messages, list)
        for msg in messages:
            assert isinstance(msg, dict)
            assert "id" in msg
            assert "header" in msg
            assert "body" in msg
