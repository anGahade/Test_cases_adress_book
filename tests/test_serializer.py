import pytest
from contact.models import Contact, ContactGroup
from contact.serializers import ContactSerializer, ContactGroupSerializer


@pytest.mark.django_db
def test_contact_serialization():
    # Створення об'єкта Contact
    contact = Contact(
        first_name="John",
        last_name="Doe",
        country="USA",
        city="New York",
        street="123 Main St",
        url="http://example.com",
        phone="555-1234",
    )

    # Серіалізація об'єкта за допомогою ContactSerializer
    serializer = ContactSerializer(contact)
    serialized_data = serializer.data

    # Перевірка коректності отриманого JSON
    expected_json_1 = {
        "first_name": "John",
        "last_name": "Doe",
        "country": "USA",
        "city": "New York",
        "street": "123 Main St",
        "url": "http://example.com",
        "phone": "555-1234",
        "image": None,
    }

    assert serialized_data == expected_json_1


@pytest.mark.django_db
def test_contact_group_serialization():
    # Створення об'єкта ContactGroup
    group = ContactGroup(name="My Group")

    # Збереження групи контактів, щоб отримати призначений id
    group.save()

    # Створення об'єктів контактів
    contact1 = Contact(
        first_name="John",
        last_name="Doe",
        country="USA",
        city="New York",
        street="123 Main St",
        url="http://example.com",
        phone="555-1234",
    )
    contact2 = Contact(
        first_name="Jane",
        last_name="Doe",
        country="Canada",
        city="Toronto",
        street="456 Maple St",
        url="http://example.net",
        phone="555-5678",
    )

    # Збереження кожного контакту
    contact1.save()
    contact2.save()

    # Додавання контактів до групи
    group.contacts.add(contact1, contact2)

    # Серіалізація об'єкта групи за допомогою ContactGroupSerializer
    serializer = ContactGroupSerializer(group)
    serialized_data = serializer.data

    # Перевірка коректності отриманого JSON
    expected_json = {
        "id": group.id,
        "name": "My Group",
        "contacts": [
            {
                "id": contact1.id,
                "first_name": "John",
                "last_name": "Doe",
                "country": "USA",
                "city": "New York",
                "street": "123 Main St",
                "url": "http://example.com",
                "phone": "555-1234",
                "image": None,
            },
            {
                "id": contact2.id,
                "first_name": "Jane",
                "last_name": "Doe",
                "country": "Canada",
                "city": "Toronto",
                "street": "456 Maple St",
                "url": "http://example.net",
                "phone": "555-5678",
                "image": None,
            },
        ],
    }

    assert serialized_data == expected_json
