from django.test import TestCase
from .models import Guardian
from phonenumber_field.phonenumber import PhoneNumber
from django.core.exceptions import ValidationError

class GuardianModelTestCase(TestCase):
    def setUp(self):
        self.guardian = Guardian(
            first_name="Angela",
            last_name="Adisa", 
            national_id="35056144",
            number_of_children=2,
            is_eligible=True,
            phone_number = PhoneNumber.from_string("+254713030706"),
        )
        self.guardian.save()

    def test_guardian_creation(self):
        self.assertEqual(self.guardian.first_name, "Angela")
        self.assertEqual(self.guardian.last_name, "Adisa")
        self.assertEqual(self.guardian.national_id, "35056144")
        self.assertEqual(self.guardian.number_of_children, 2)
        self.assertTrue(self.guardian.is_eligible)
        self.assertEqual(str(self.guardian.phone_number), "+254713030706")

    def test_guardian_str_method(self):
        expected_str = "Angela Adisa" 
        self.assertEqual(str(self.guardian), expected_str)

    def test_duplicate_phone_number(self):
        duplicate_guardian = Guardian(
            first_name="James",
            last_name="Ligami",
            national_id="12345678",
            number_of_children=1,
            is_eligible=True,
            phone_number = PhoneNumber.from_string("+254713030706"),
        )
        with self.assertRaises(ValidationError):
            duplicate_guardian.full_clean()

    def test_invalid_phone_number(self):
        invalid_phone_guardian = Guardian(
            first_name="Kyle",
            last_name="Jesse",
            national_id="12345678",
            number_of_children=3,
            is_eligible=True,
            phone_number=PhoneNumber.from_string("+25478905645"),
        )
        with self.assertRaises(ValidationError):
            invalid_phone_guardian.full_clean()

    def test_negative_number_of_children(self):
        negative_children_guardian = Guardian(
            first_name="Swahili",
            last_name="Michael",
            national_id="87654321",
            number_of_children=-1,
            is_eligible=True,
            phone_number=PhoneNumber.from_string("+254712345678"),
        )
        with self.assertRaises(ValidationError):
            negative_children_guardian.full_clean()

    def test_unique_national_id(self):
        duplicate_national_id_guardian = Guardian(
            first_name="Brian",
            last_name="Tongi",
            national_id="35056144",
            number_of_children=1,
            is_eligible=True,
            phone_number=PhoneNumber.from_string("+254711789034"),
        )
        with self.assertRaises(ValidationError):
            duplicate_national_id_guardian.full_clean()

    def test_blank_first_name(self):
        blank_first_name_guardian = Guardian(
            first_name="",  
            last_name="Mahiva",
            national_id="99999999",
            number_of_children=2,
            is_eligible=True,
            phone_number=PhoneNumber.from_string("+254710000000"),
        )
        with self.assertRaises(ValidationError):
            blank_first_name_guardian.full_clean()
