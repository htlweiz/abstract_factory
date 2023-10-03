"""Concrete Json implementation of Message

@author Matthias Derler
"""
import json
from typing import List

from .._message import AbstractMessage


class JsonMessage(AbstractMessage):
    def __init__(self, json_file: str) -> None:
        self._json_file = json_file
        open(json_file, 'w+').close()

    def getMessages(self) -> List[object]:
        """Retrieve all Message

        Returns:
            List[object]: list of message representative objects in form:
                          { "id": id, "header": header, "body": body }
        """
        messages = []
        try:
            with open(self._json_file, 'r') as json_fr:
                message_obj = json.loads(json_fr.read())
                messages = message_obj["messages"]
        except json.JSONDecodeError as e:
            print(e)
            return []
        return messages

    def postMessage(self, header: str, body: str) -> None:
        """Post new message

        Args:
            header (str): message header text
            body (str): message body text
        """
        messages = self.getMessages()
        print(messages)
        messages.append({"header": header, "body": body})
        with open(self._json_file, 'w+') as json_fw:
            print(json.dumps({"messages": messages}))
            json_fw.write(json.dumps({"messages": messages}))
