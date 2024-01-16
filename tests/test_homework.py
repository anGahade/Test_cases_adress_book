import unittest
from django.test import TestCase
from contact.models import Contact, ContactActivityLog


class TestContactSave(TestCase):

    def test_new_contact_creates_activity_log_entry(self):
        # Створюємо новий контакт
        new_contact = Contact(first_name="John", last_name="Doe", country="Ukraine")

        # Зберігаємо контакт
        new_contact.save()

        # Перевіряємо, чи створено відповідний запис в ContactActivityLog
        activity_log_entry = ContactActivityLog.objects.filter(contact=new_contact, activity_type="CREATED").first()
        self.assertIsNotNone(activity_log_entry)
        self.assertEqual(activity_log_entry.details, f"Contact {new_contact.first_name} "
                                                     f"{new_contact.last_name} was created.")

    def test_edited_contact_creates_activity_log_entry(self):
        # Створюємо і зберігаємо контакт, щоб мати PK
        existing_contact = Contact(first_name="Jane", last_name="Doe", country="USA")
        existing_contact.save()

        # Редагуємо контакт
        existing_contact.first_name = "Jane Updated"
        existing_contact.save()

        # Перевіряємо, чи створено відповідний запис в ContactActivityLog
        activity_log_entry = ContactActivityLog.objects.filter(contact=existing_contact, activity_type="EDITED").first()
        self.assertIsNotNone(activity_log_entry)
        self.assertIn("Contact", activity_log_entry.details)
        self.assertIn("was updated", activity_log_entry.details)


if __name__ == '__main__':
    unittest.main()
