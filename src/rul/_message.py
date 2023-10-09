""" This is the abstract message module

@author Robert Ulmer
"""

from abc import ABC, abstractmethod
from typing import List


class AbstractMessage(ABC):
    """
    Abstract Base Class for the Message interface
    """

    @abstractmethod
    def get_messages(self) -> List[object]:
        """Retrieve all Message

        Returns:
            List[object]: list of message representative objects in form:
                          { "id": id, "header": header, "body": body }
        """

    @abstractmethod
    def post_message(self, header: str, body: str) -> None:
        """Post new message

        Args:
            header (str): message header text
            body (str): message body text
        """
