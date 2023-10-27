"""Concrete JSON implementation of Message

@author Kevin Schneidhofer
"""
import json
from typing import List

from .._message import AbstractMessage
from ._model import JSON_Message


class JSONMessage(AbstractMessage):

    def __init__(self, db_file: str):
        """initialize Message and bind to db

        Args:
            db_file (str): .json db file
        """
        self._db = db_file

        try:
            open(db_file, 'x')
        except FileExistsError:
            pass

    def getMessages(self) -> List[object]:
        """Retrieve all Message

        Returns:
            List[object]: list of message representative objects in form:
                          { "id": id, "header": header, "body": body }
        """

        return_value = []

        with open(self._db, 'r') as json_file:
            first_char = json_file.read(1)

            if not first_char:
                return return_value
            else:
                with open(self._db, 'r') as json_file:
                    data = json.load(json_file)
                    jsonData = data.get("messages", [])
                    for row in jsonData:
                        return_value.append(row)
                return return_value

    def postMessage(self, header, body):
        """Post new message

        Args:
            header (str): message header text
            body (str): message body text
        """

        json_start = {"messages": []}
        json_content_messages = []

        with open(self._db, 'r') as json_file:
            try:
                json_content = json.load(json_file)
                message_list = json_content.get("messages")
                last_id = message_list[-1].get("id")
            except json.decoder.JSONDecodeError:
                json_content = json_start
                last_id = 0

        message_id = last_id + 1

        message = JSON_Message().create_json_dict()
        message['id'] = message_id
        message['header'] = header
        message['body'] = body

        json_content_messages = json_content.get("messages", [])
        json_content_messages.append(message)

        json_content["messages"] = json_content_messages

        with open(self._db, 'w') as json_file:
            json.dump(json_content, json_file, indent=4)
