"""
JSON implementation of Message
"""

from typing import List

import json
from .._message import AbstractMessage
from ._model import JSONMessage

class JSONMessage(AbstractMessage):
    def __init__(self, db_file: str):
        """initialize Message and bind to db

        Args:
            db_file (str): json file
        """
        self._db = db_file

    def getMessages(self) -> List[object]:
        """Retrieve all Message

        Returns:
            List[object]: list of message representative objects in form:
                          { "id": id, "header": header, "body": body }
        """
        return_value = []
        file = open(self._db)
        data = json.load(file)
        for i in data:
            # see how the message is built
            print(i)
        #for message in JSONMessage.select():
        #    return_value.append(
        #        {"id": message.id, "header": message.header, "body": message.body}
        #    )
        return return_value

    def postMessage(self, header, body):
        """Post new message

        Args:
            header (str): message header text
            body (str): message body text
        """

        # read input
        # read id of last message
        # create new id with old_id +1 
        # add new entry
        # save

        message = JSONMessage(header, body)
        with open(self._db, 'a') as file:
            json.dump(message, file)
