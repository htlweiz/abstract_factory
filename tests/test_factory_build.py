from rul.main import PeeWeeMessageFactory, AlchemyMessageFactory


def test_build_message():
    for factory in [PeeWeeMessageFactory, AlchemyMessageFactory]:
        message = factory().buildMessage()
        assert message is not None
