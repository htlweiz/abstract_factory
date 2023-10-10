""" This is the abstract message module

@author Simon Posch
"""

from abc import ABC, abstractmethod
from typing import List


class AbstractMessage(ABC):
    """Abstract Base Class for the Message interface"""

    @abstractmethod
    def getMessages(self) -> List[object]:
        """Retrieve all Message

        Returns:
            List[object]: list of message representative objects in form:
                          { "id": id, "header": header, "body": body }
        """
        pass

    @abstractmethod
    def postMessage(self, header: str, body: str) -> None:
        """Post new message

        Args:
            header (str): message header text
            body (str): message body text
        """
        pass
