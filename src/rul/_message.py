from abc import ABC, abstractmethod
from typing import List
import json

class AbstractMessage(ABC):
    @abstractmethod
    def getMessages(self) -> List[object]:
        pass

    @abstractmethod
    def postMessage(self, header: str, body: str) -> None:
        pass

class JsonMessage(AbstractMessage):
    def __init__(self, filename):
        self.filename = filename
        self.data = None
        self.initialize()

    def initialize(self):
        try:
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {}

    def save(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)

    def getMessages(self) -> List[object]:
        return list(self.data.values())

    def postMessage(self, header: str, body: str) -> None:
        message_id = len(self.data) + 1
        new_message = {
            "id": message_id,
            "header": header,
            "body": body
        }
        self.data[message_id] = new_message
        self.save()