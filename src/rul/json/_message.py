"""" Json Message Module."""

import json
from typing import List
from .._message import AbstractMessage


class JsonMessage(AbstractMessage):
    """
    A class representing message handling using a JSON file.

    This class provides methods to load, save, retrieve, and post messages to JSON-File.

    Attributes:
        json_file (str): The path to the JSON file to read/write messages.
        messages (List[dict]): A list of message dictionaries loaded from the JSON file.
    """

    def __init__(self, json_file: str):
        """
        Initialize a JsonMessage instance.

        Args:
            json_file (str): The path to the JSON file to read/write messages.
        """
        self.json_file = json_file
        self.messages = self._load_messages()

    def _load_messages(self):
        """
        Load messages from the specified JSON file.

        Returns:
            List[dict]: A list of message dictionaries loaded from the JSON file.
        """
        try:
            with open(self.json_file, 'r', encoding='utf-8') as file:
                data = file.read()
                print("Loaded data from file:", data)
                messages = json.loads(data)
                return messages
        except FileNotFoundError:
            return []
        except json.JSONDecodeError as decode_error:
            print("Error decoding JSON:", str(decode_error))
            return []

    def _save_messages(self):
        """
        Save the current messages to the specified JSON file.
        """
        with open(self.json_file, 'w', encoding='utf-8') as file:
            json.dump(self.messages, file, indent=4)

    def getMessages(self) -> List[object]:
        """
        Retrieve all messages.

        Returns:
            List[dict]: A list of message dictionaries.
        """
        return self.messages

    def postMessage(self, header: str, body: str) -> None:
        """
        Post a new message.

        Args:
            header (str): The message header text.
            body (str): The message body text.
        """
        if not self.messages:
            message_id = 1
        else:
            message_id = max(msg.get('id', 0) for msg in self.messages) + 1

        new_message = {"id": message_id, "header": header, "body": body}
        self.messages.append(new_message)
        self._save_messages()
