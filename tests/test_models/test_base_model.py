#!/usr/bin/env python3
""" unittest for base model """


from datetime import datetime
import inspect
from models.base_model import BaseModel
import pep8 as pycodestyle
import unittest
from unittest import mock


module_doc = models.base_model.__doc__

class Testforpycodestyle(unittest.TestCase):
    """Tests to check the documentation and style of BaseModel class"""

    @classmethod
    def setUpClass(self):
        """Set up for docstring tests"""
        BaseModel = BaseModel()
        self.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_pep8_conformance(self):
        """Test that models/base_model.py conforms to PEP8."""
        for path in ['models/base_model.py',
                     'tests/test_models/test_base_model.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertIsNot(module_doc, None,
                         "base_model.py needs a docstring")
        self.assertTrue(len(module_doc) > 1,
                        "base_model.py needs a docstring")

    def test_class_docstring(self):
        """Test for the BaseModel class docstring"""
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel class needs a docstring")

    def test_func_docstrings(self):
        """Test for the presence of docstrings in BaseModel methods"""
        for func in self.base_funcs:
            with self.subTest(function=func):
                self.assertIsNot(
                    func[1].__doc__,
                    None,
                    "{:s} method needs a docstring".format(func[0])
                )
                self.assertTrue(
                    len(func[1].__doc__) > 1,
                    "{:s} method needs a docstring".format(func[0])
                )



""" define to tesst out putwith type """

class TestBaseModel(unittest.TestCase):
    """ define unittests for base model """

    def setUp(self):
        """ setup for the proceeding tests """
        model = BaseModel()
        model.name = "My First Model"
        model.my_number = 89

    def test_id_type(self):
        """ test for id type """
        self.assertEqual(type(model.id), str)

    def test_created_at_type(self):
        """ test for created at type """
        self.assertEqual(type(model.created_at), datetime)

    def test_updated_at_type(self):
        """ test for updated at type """
        self.assertIsInstance(model.updated_at, datetime)

    def test_name_type(self):
        """ test for name type """
        self.assertEqual(type(model.name), str)

    def test_my_number_type(self):
        """ test for my number type """
        self.assertEqual(type(model.my_number), int)

    def test_save_updates_updated_at(self):
        """ test for save updated at """
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict_returns_dict(self):
        """ test for to dict return type """
        self.assertIsInstance(type(model.to_dict()), dict)

    def test_to_dict_contains_correct_keys(self):
        """ test for dict containing correct keys """
        model_dict = model.to_dict()
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('name', model_dict)
        self.assertIn('my_number', model_dict)
        self.assertIn('__class__', model_dict)

    def test_to_dict_created_time_at_format(self):
        """ test for created at format """
        model_dict = model.to_dict()
        created_at = model_dict['created_at']
        self.assertEqual(created_at, model.created_at.isoformat())

    def test_to_dict_updated_at_format(self):
        """ test for updated at format """
        model_dict = model.to_dict()
        updated_at = model_dict['updated_at']
        self.assertEqual(updated_at, model.updated_at.isoformat())


class TestBaseModelTwo(unittest.TestCase):
    """ define unittests for base model two """

    def setUp(self):
        """ setup for proceeding tests two """
        my_model = BaseModel()

    def test_id_generation(self):
        """ test for id gen type """
        self.assertIsInstance(my_model.id, str)

    def test_str_representation(self):
        """ test for str rep """
        expected = "[BaseModel] ({}) {}".format(
            my_model.id, my_model.__dict__)
        self.assertIsInstance(str(my_model), expected)

    def test_to_dict_method(self):
        """ test for to dict method """
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict['created_at'], 'BaseModel')
        self.assertIsInstance(my_model_dict['updated_at'], 'BaseModel')
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')

    def test_from_dict_method(self):
        """ test for from dict method """
        my_model_dict = my_model.to_dict()
        my_new_model = BaseModel(**my_model_dict)
        self.assertEqual(my_new_model.id, my_model.id)
        self.assertEqual(my_new_model.created_at, my_model.created_at)
        self.assertEqual(my_new_model.updated_at, my_model.updated_at)

class TestBaseMode_file_storage(unittest.TestCase):
    """Test the BaseModel class"""
    @mock.patch('models.storage')
    def test_instantiation(self, mock_storage):
        """Test that object is correctly created"""
        inst = BaseModel()
        self.assertIs(type(inst), BaseModel)
        inst.name = "My_First_Model"
        inst.number = 89
        attrs_types = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "name": str,
            "number": int
        }
        for attr, typ in attrs_types.items():
            with self.subTest(attr=attr, typ=typ):
                self.assertIn(attr, inst.__dict__)
                self.assertIs(type(inst.__dict__[attr]), typ)
        self.assertTrue(mock_storage.new.called)
        self.assertEqual(inst.name, "My_First_Model")
        self.assertEqual(inst.number, 89)
     
    def test_save(self, mock_storage):
        """Test that save method updates `updated_at` and calls
        `storage.save`"""
        inst = BaseModel()
        old_created_at = inst.created_at
        old_updated_at = inst.updated_at
        inst.save()
        new_created_at = inst.created_at
        new_updated_at = inst.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(old_created_at, new_created_at)
        self.assertTrue(mock_storage.save.called)
if __name__ == "__main__":
    unittest.main()
