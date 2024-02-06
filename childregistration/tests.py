from django.test import TestCase
from datetime import date
from django.core.exceptions import ValidationError
from .models import ChildRegistration

class ChildRegistrationTestCase(TestCase):
    def setUp(self):
        self.child = ChildRegistration(
            first_name="Jane",
            last_name="Ndiragu",
            gender="Female",
            date_of_birth=date(2020, 5, 15),
        )
        self.child.save()

    def test_age(self):
        today = date.today()
        expected_age = today.year - self.child.date_of_birth.year
        self.assertEqual(self.child.age(), expected_age)

    def test_missing_required_fields(self):
      with self.assertRaises(ValidationError):
        child = ChildRegistration()
        child.full_clean()

    def test_gender_lowercase(self):
        self.assertEqual(self.child.gender, "female")

    def test_str_method(self):
        expected_str = f"{self.child.first_name} {self.child.last_name} (Gender: {self.child.gender}, Age: {self.child.age()})"
        self.assertEqual(str(self.child), expected_str)

    def test_created_at_auto_now_add(self):
        self.assertIsNotNone(self.child.created_at)

    def test_updated_at_auto_now_add(self):
        self.assertIsNotNone(self.child.updated_at)

    def test_date_of_birth_in_past(self):
        today = date.today()
        self.assertTrue(self.child.date_of_birth < today)

    def test_invalid_date_of_birth(self):
      with self.assertRaises(ValidationError):
        child = ChildRegistration(
            first_name="Anna",
            last_name="Wambua",
            gender="Female",
            date_of_birth="invalid_date",
        )
        child.full_clean()


    def test_invalid_gender_choice(self):
      with self.assertRaises(ValidationError):
        child = ChildRegistration(
            first_name="James",
            last_name="Atieno",
            gender="invalid",
            date_of_birth=date(2021, 11, 21),
        )
        child.full_clean()  