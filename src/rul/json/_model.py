"""
Model for JSON database.
"""

class JSONMessage():
    def __init__(self, header, subject, body) -> None:
        self.header = header
        self.body = body