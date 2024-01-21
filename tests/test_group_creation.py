import pytest
from contact.models import ContactGroup, Contact


@pytest.mark.django_db
def test_create_group_and_add_contacts():
    # Створення нової групи
    group = ContactGroup.objects.create(name="Test Group")

    # Створення контактів
    contact1 = Contact.objects.create(first_name="John", last_name="Doe", phone="555-1234")
    contact2 = Contact.objects.create(first_name="Jane", last_name="Doe", phone="555-5678")

    # Додавання контактів до групи
    group.contacts.add(contact1, contact2)

    # Перевірка, чи контакти коректно додані до групи
    assert contact1 in group.contacts.all()
    assert contact2 in group.contacts.all()
    assert group.contacts.count() == 2
