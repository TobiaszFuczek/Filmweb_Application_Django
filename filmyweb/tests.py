from django.test import TestCase

from filmyweb.models import Film


#from .models import Film


class MyModelTestCase(TestCase):

     def setUp(self):
         #self.assertEquals("1","1")
         Film.objects.create(title="Test", description="Test Description")

    def test_model_creation(self):
        obj = Film.objects.get(title="Test")

        self.assertEqual(obj.description, "Test Description")


    def test_model_update(self):
        obj = Film.objects.get(title="Test")

        obj.description = "Updated Description"

        obj.save()

        updated_obj = Film.objects.get(title="Test")

        self.assertEqual(updated_obj.description, "Updated Description")

    def test_model_deletion(self):
        obj = Film.objects.get(title="Test")

        obj.delete()

        with self.assertRaises(Film.DoesNotExist):
            Film.objects.get(title="Test")
