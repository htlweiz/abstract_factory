"""
Model for JSON database.
"""


class JSONModel():
    def __init__(self, _id, header, body) -> None:
        self.id = _id
        self.header = header
        self.body = body

    def ToDict(self):
        return {
            'id': self.id,
            'header': self.header,
            'body': self.body
        }
