"""Concrete PeeWee implementation of Message

@author Simon Posch
"""
import json
from typing import List

class JSONMessage:
    def __init__(self, json_file: str):
        """Initialize Message and bind to JSON file

        Args:
            json_file (str): JSON file to store messages
        """
        self.json_file = json_file
        self.messages = []
        self.load_messages()

    def load_messages(self):
        """Load messages from the JSON file."""
        try:
            with open(self.json_file, 'r') as file:
                self.messages = json.load(file)
        except FileNotFoundError:
            self.messages = []

    def save_messages(self):
        """Save messages to the JSON file."""
        with open(self.json_file, 'w') as file:
            json.dump(self.messages, file)

    def getMessages(self) -> List[object]:
        """Retrieve all messages.

        Returns:
            List[object]: List of message representative objects in the form:
            { "id": id, "header": header, "body": body }
        """
        return self.messages

    def postMessage(self, header, body):
        """Post a new message.

        Args:
            header (str): Message header text.
            body (str): Message body text.
        """
        message = {"id": len(self.messages) + 1, "header": header, "body": body}
        self.messages.append(message)
        self.save_messages()

if __name__ == "__main__":
    json_message = JSONMessage("messages.json")
    json_message.postMessage("Header 1", "Body 1")
    json_message.postMessage("Header 2", "Body 2")

    messages = json_message.getMessages()
    for message in messages:
        print(message)
