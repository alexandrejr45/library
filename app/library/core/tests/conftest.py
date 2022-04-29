import uuid

import pytest
from datetime import date
from library.core.models import Author


@pytest.fixture
def author_model():
    Author.objects.create(name='Amaral', last_name='Macedo')
    return Author.objects.get(name='Amaral')


@pytest.fixture
def author_payload_valid():
    return {
        'name': 'Amaral',
        'last_name': 'Macedo'
    }


@pytest.fixture
def author_payload_invalid():
    return {
        'name': 'Amaral',
        'last_name': (
            'Lorem ipsum dolor sit amet, consectetur adipiscing'
            'elit. Sed id molestie dolor. Sed placerat sagittis mi,'
            'lobortis rutrum augue bibendum ac. Nulla ac fermentum'
            'urna. Nulla sed turpis ultricies, sollicitudin mi eu,'
            'convallis ante. Proin ullamcorper enim eu est cras.'
        )
    }


@pytest.fixture
def book_payload_valid(author_model):
    return {
        'name': 'The best book ever',
        'edition': '1st forever',
        'publication_year': date.today(),
        'isbn': str(uuid.uuid4()),
        'authors': [author_model.pk]
    }


@pytest.fixture
def book_payload_invalid():
    return {
        'name': 'The best book ever',
        'edition': '1st forever',
        'publication_year': date.today(),
        'isbn': str(uuid.uuid4()),
        'authors': 1
    }
