from rul.main import PeeWeeMessageFactory, AlchemyMessageFactory


def test_post_message_with_data():
    for factory in [PeeWeeMessageFactory, AlchemyMessageFactory]:
        message = factory().buildMessage()

        initial_messages = message.getMessages()
        new_message_header = "Test Header"
        new_message_body = "Test Body"

        message.postMessage(new_message_header, new_message_body)
        updated_messages = message.getMessages()

        # Check if the new message is in the updated messages
        new_message = None
        for msg in updated_messages:
            if msg["header"] == new_message_header and msg["body"] == new_message_body:
                new_message = msg
                break
        assert new_message is not None
