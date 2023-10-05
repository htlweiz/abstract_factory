import unittest
import os
from src.rul.json._message import JsonMessage


class TestJsonMessageMethods(unittest.TestCase):

    def setUp(self):
        """
         Set up the test environment before each test.
        """
        self.test_file = "test_messages.json"
        self.obj = JsonMessage()
        self.obj.initialize(self.test_file)

    def tearDown(self):
        """
         Remove the test file after each test. This is called after each test.
        """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_get_messages_empty(self):
        """
         Tests the getMessages method when there are no messages in the object. This is a no - op
        """
        data = self.obj.getMessages()
        self.assertEqual(data, [])

    def test_post_message_and_get_message(self):
        """
         Test postMessage and getMessage from Message object.
         Ensures that the message is correctly stored and retrieved.
        """
        header = "Test Header"
        body = "Test Body"
        self.obj.postMessage(header, body)
        messages = self.obj.getMessages()
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0]['header'], header)
        self.assertEqual(messages[0]['body'], body)
        self.assertEqual(messages[0]['id'], 1)

    def test_post_multiple_messages(self):
        """
         Post multiple messages to the message list and verify they are posted correctly.
        """
        headers = ["Header1", "Header2"]
        bodies = ["Body1", "Body2"]

        for i in range(2):
            self.obj.postMessage(headers[i], bodies[i])
        messages = self.obj.getMessages()
        self.assertEqual(len(messages), 2)

        for i, message in enumerate(messages):
            self.assertEqual(message['header'], headers[i])
            self.assertEqual(message['body'], bodies[i])
            self.assertEqual(message['id'], i+1)


if __name__ == '__main__':
    unittest.main()
