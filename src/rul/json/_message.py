import json
from typing import List

class AbstractMessage:
    pass

class JSONMessage(AbstractMessage):
    def __init__(self, json_file: str):
        self.json_file = json_file
        self.messages = []

        try:
            with open(json_file, 'r') as file:
                self.messages = json.load(file)
        except FileNotFoundError:
            self.messages = []

    def getMessages(self) -> List[object]:
        # Import AbstractMessage where it's used
        from ._message import AbstractMessage
        return self.messages

    def postMessage(self, header: str, body: str) -> None:
        # Import AbstractMessage where it's used
        from ._message import AbstractMessage

        new_message = {"header": header, "body": body}
        self.messages.append(new_message)

        with open(self.json_file, 'w') as file:
            json.dump(self.messages, file)
            

    def saveMessagesToFile(self):
        with open(self.json_file, 'w') as file:
            json.dump(self.messages, file)

