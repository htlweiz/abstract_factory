"""
Test cases for the postMessage method.
"""

from rul.json import JSONMessage
from rul.json import JSONModel


class TestCases:
    def test_post_valid(self):
        """Test if the data has been saved to the json"""
        filename = "test_db.json"
        context = ""

        form = [{
            'id': 1,
            'header': 'Subj 1',
            'body': 'body 1'
        }, {
            'id': 2,
            'header': 'Subj 2',
            'body': 'body 2'
        }]

        with open(filename, 'r') as file:
            context = file.read()

            jsonM = JSONMessage(filename)
            jsonM.postMessage("Subj 2", "body 2")
            result = jsonM.getMessages()

            assert form[0] == result[0]
            assert form[1] == result[1]

        with open(filename, 'w') as file:
            file.write(context)

    def test_new_id(self):
        """Test if the new id is higher than the old id"""
        filename = "test_db.json"
        context = ""

        with open(filename, 'r') as file:
            context = file.read()

            jsonM = JSONMessage(filename)
            old_id = jsonM.getLastId()

            assert old_id == 1
            jsonM.postMessage("Subj %d" % (old_id + 1), "body %d" % (old_id + 1))
            new_id = jsonM.getLastId()

            assert old_id != new_id
            assert old_id + 1 == new_id

        with open(filename, 'w') as file:
            file.write(context)

    def test_get_Message_valid(self):
        """Testing if valid json file could be read.
        """

        dict = {
            'id': 1,
            'header': 'Subj 1',
            'body': 'body 1'
        }
        jsonM = JSONMessage("test_db.json")
        result = jsonM.getMessages()
        assert result[0] == dict

    def test_get_Message_invalid(self):
        """Testing if invalid json file could be read.
        """
        jsonM = JSONMessage("nonexistent.json")
        result = jsonM.getMessages()
        assert result == []

    def test_model(self):
        jsonModel = JSONModel("2", "Sub 2", "body 2")
        result = jsonModel.ToDict()
        dict = {
            'id': '2',
            'header': 'Sub 2',
            'body': 'body 2'
        }
        assert result == dict
