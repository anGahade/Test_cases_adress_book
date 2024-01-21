import pytest
from contact.models import Contact
from contact.serializers import ContactSerializer


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
    expected_json = {
        "first_name": "John",
        "last_name": "Doe",
        "country": "USA",
        "city": "New York",
        "street": "123 Main St",
        "url": "http://example.com",
        "phone": "555-1234",
        "image": None,
    }

    assert serialized_data == expected_json
