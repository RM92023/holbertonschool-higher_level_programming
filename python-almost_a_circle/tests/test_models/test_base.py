import unittest
from models.base import Base
import json


class TestBase(unittest.TestCase):

    def test_base_id_generation(self):
        base1 = Base()
        base2 = Base()
        base3 = Base(89)
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 89)

    def test_base_to_json_string_none(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_base_to_json_string_empty_list(self):
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_base_to_json_string_with_data(self):
        json_string = Base.to_json_string([{'id': 12}])
        self.assertEqual(json_string, '[{"id": 12}]')

    def test_base_to_json_string_with_data_returning_string(self):
        json_string = Base.to_json_string([{'id': 12}])
        self.assertIsInstance(json_string, str)

    def test_base_from_json_string_none(self):
        result = Base.from_json_string(None)
        self.assertEqual(result, [])

    def test_base_from_json_string_empty_list(self):
        result = Base.from_json_string("[]")
        self.assertEqual(result, [])

    def test_base_from_json_string_with_data(self):
        result = Base.from_json_string('[{"id": 89}]')
        self.assertEqual(result, [{'id': 89}])

    def test_base_from_json_string_with_data_returning_list(self):
        result = Base.from_json_string('[{"id": 89}]')
        self.assertIsInstance(result, list)


class TestToJsonString(unittest.TestCase):
    def test_to_json_string_empty_list(self):
        # Prueba cuando se pasa una lista vacía
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_none(self):
        # Prueba cuando se pasa None como argumento
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_to_json_string_single_dict(self):
        # Prueba cuando se pasa una lista con un solo diccionario
        input_list = [{'name': 'John', 'age': 30}]
        expected_result = json.dumps(input_list)
        result = Base.to_json_string(input_list)
        self.assertEqual(result, expected_result)
    
    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + '.json'
        with open(filename, 'w') as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                list_dict = [o.to_dictionary() for o in list_objs]
                json_file.write(Base.to_json_string(list_dict))


    def test_to_json_string_multiple_dicts(self):
        # Prueba cuando se pasa una lista con varios diccionarios
        input_list = [{'name': 'John', 'age': 30}, {'name': 'Jane', 'age': 25}]
        expected_result = json.dumps(input_list)
        result = Base.to_json_string(input_list)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
