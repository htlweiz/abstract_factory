""" Model for sqlalchemy message

@author Robert Ulmer
"""

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """
    Base
    """


class Message(Base):
    """
    Message
    """

    __tablename__ = "alchemymessage"

    message_id: Mapped[int] = mapped_column(primary_key=True)
    header_text: Mapped[str] = mapped_column(String(30))
    body_text: Mapped[str] = mapped_column(String(500))
