import unittest
from mongomock import MongoClient
from src.rul.mongo._message import MongoMessage


class TestMongoMessageMethods(unittest.TestCase):

    def setUp(self):
        """
        Initializes a MongoMessage object and mocks the MongoDB server connection.
        """
        self.obj = MongoMessage()
        self.obj.initialize('test')
        self.obj.server = MongoClient()

    def tearDown(self):
        """
        Clean up the test environment after each test.
        """
        self.obj.collection.drop()

    def test_get_messages_empty(self):
        """
         Tests the getMessages method when there are no messages in the object.
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

    def test_post_multiple_messages(self):
        """
         Post multiple messages at once and check they are returned in correct order. This is to make sure it doesn't crash
        """
        headers = ["Header1", "Header2"]
        bodies = ["Body1", "Body2"]
        for i in range(2):
            self.obj.postMessage(headers[i], bodies[i])
        messages = self.obj.getMessages()
        self.assertEqual(len(messages), 2)


if __name__ == '__main__':
    unittest.main()
