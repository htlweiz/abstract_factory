""" Model for peewee message

@author Robert Ulmer
"""

from peewee import CharField, Model


class OrmMessage(Model):
    """
    OrmMessage
    """

    header = CharField()
    body = CharField()
