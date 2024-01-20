import unittest
from django.test import TestCase
from unittest.mock import patch
from contact.models import Contact, ContactActivityLog


class TestContactSave(TestCase):

    @patch('contact.models.ContactActivityLog.objects.create')
    def test_new_contact_creates_activity_log_entry(self, mock_create):
        # Створюємо новий контакт
        new_contact = Contact(first_name="John", last_name="Doe", phone="12345678")

        # Зберігаємо контакт
        new_contact.save()

        # Перевіряємо, чи створено відповідний запис в ContactActivityLog
        mock_create.assert_called_once_with(
            contact=new_contact,
            activity_type="CREATED",
            details="Contact John Doe was created."
        )


# Запустіть тести
if __name__ == '__main__':
    unittest.main()
