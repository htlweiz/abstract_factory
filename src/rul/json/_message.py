import json
from typing import List

from .._message import AbstractMessage


class JsonMessage(AbstractMessage):
    def __init__(self, json_file: str) -> None:
        """initialize Message and bind to db

        Args:
            json_file (str): json file
        """
        self.json_file = json_file

    def initialize(self):
        open(self.json_file, "w")

    def getMessages(self) -> List[object]:
        pass

    def postMessage(self, header: str, body: str) -> None:
        pass
