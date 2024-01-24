import pytest
from django.db import IntegrityError
from django.urls import reverse
from rest_framework.test import APIClient

from contact.models import Contact


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def contact_factory(**kwargs):
    def factory(**data):
        return Contact.objects.create(**data)

    return factory


@pytest.mark.django_db
def test_filter_by_first_name(api_client, contact_factory):
    contact_1 = contact_factory(first_name='Anton', last_name='Bob')
    contact_2 = contact_factory(first_name='Daria', last_name='Smith')

    response = api_client.get(reverse('contact-list'), {'first_name': 'Anton'})
    assert response.status_code == 200
    assert len(response.data) == 1

    assert response.data[0]['first_name'] == contact_1.first_name


@pytest.mark.django_db
def test_filter_by_last_name(api_client, contact_factory):
    contact_1 = contact_factory(first_name='Anton', last_name='Bob')
    contact_2 = contact_factory(first_name='Daria', last_name='Smith')

    response = api_client.get(reverse('contact-list'), {'last_name': 'Bob'})
    assert response.status_code == 200
    assert len(response.data) == 1

    assert response.data[0]['last_name'] == contact_1.last_name


@pytest.mark.django_db
def test_unique_contact():
    #перший контакт
    Contact.objects.create(
        first_name="John",
        last_name="Doe",
        phone="555-1234"
    )

    # Спроба створити контакт з тим самим ім'ям та прізвищем
    with pytest.raises(IntegrityError):
        Contact.objects.create(
            first_name="John",
            last_name="Doe",
            phone="555-5678"
        )
