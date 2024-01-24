import unittest

import pytest
from django.test import TestCase
from unittest.mock import patch
from contact.models import Contact, ContactActivityLog
from contact.views import delete_contact_view


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


@pytest.mark.django_db
def test_delete_contact(mocker):
    # Створюємо новий контакт
    contact = Contact.objects.create(
        first_name="John",
        last_name="Doe",
        phone="555-1234"
    )

    # Mock-об'єкт для методу видалення
    mock_delete_method = mocker.patch.object(Contact, 'delete')

    # Викликаємо функцію видалення контакту (наприклад, через вашу view-функцію)
    delete_contact_view(contact.id)

    # Перевірка, чи метод видалення був викликаний
    mock_delete_method.assert_called_once_with()

    # Перевірка, чи об'єкт не був дійсно видалений з бази даних
    assert Contact.objects.filter(id=contact.id).exists()