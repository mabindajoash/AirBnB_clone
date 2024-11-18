import unittest
from datetime import datetime
from models.base_model import BaseModel
import uuid


class TestBaseModel(unittest.TestCase):
    """Unit tests for the BaseModel class"""

    def test_init_with_kwargs(self):
        """Test initializing BaseModel with kwargs"""
        kwargs = {
            'id': str(uuid.uuid4()),
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat(),
            'name': "Test"
        }
        obj = BaseModel(**kwargs)
        self.assertEqual(obj.id, kwargs['id'])
        self.assertEqual(obj.name, "Test")
        self.assertEqual(obj.created_at.isoformat(), kwargs['created_at'])
        self.assertEqual(obj.updated_at.isoformat(), kwargs['updated_at'])

    def test_init_without_kwargs(self):
        """Test initializing BaseModel without kwargs"""
        obj = BaseModel()
        self.assertIsNotNone(obj.id)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertTrue(hasattr(obj, 'id'))

    def test_str(self):
        """Test __str__ method"""
        obj = BaseModel()
        string = f"[{obj.__class__.__name__}] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), string)

    def test_save(self):
        """Test save method updates updated_at"""
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, old_updated_at)
        self.assertTrue(obj.updated_at > old_updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], obj.__class__.__name__)
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())

    def test_to_dict_contains_all_attributes(self):
        """Test to_dict includes all instance attributes"""
        obj = BaseModel()
        obj.name = "Test"
        obj.age = 30
        obj_dict = obj.to_dict()
        self.assertIn('name', obj_dict)
        self.assertIn('age', obj_dict)
        self.assertEqual(obj_dict['name'], "Test")
        self.assertEqual(obj_dict['age'], 30)


if __name__ == '__main__':
    unittest.main()

