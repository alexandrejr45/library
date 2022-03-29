import pytest
from datetime import date
from library.core.models import Author, Book
from django.db.utils import DataError

pytestmark = pytest.mark.django_db


class TestAuthor:
    def test_should_create_author(self):
        Author.objects.create(name='Mido', last_name='Sore')

        assert Author.objects.count() == 1
        assert Author.objects.get(name='Mido').name == 'Mido'
        assert Author.objects.get(name='Mido').last_name == 'Sore'

    def test_should_not_creater_author_with_invalid_name(self):
        with(pytest.raises(DataError)):
            Author.objects.create(
                name=(
                    'Lorem ipsum dolor sit amet, consectetur adipiscing'
                    'elit. Sed id molestie dolor. Sed placerat sagittis mi,'
                    'lobortis rutrum augue bibendum ac. Nulla ac fermentum'
                    'urna. Nulla sed turpis ultricies, sollicitudin mi eu,'
                    'convallis ante. Proin ullamcorper enim eu est cras.'
                )
            )

    def test_should_not_creater_author_with_invalid_last_name(self):
        with(pytest.raises(DataError)):
            Author.objects.create(
                name='Shirazs',
                last_name=(
                    'Lorem ipsum dolor sit amet, consectetur adipiscing'
                    'elit. Sed id molestie dolor. Sed placerat sagittis mi,'
                    'lobortis rutrum augue bibendum ac. Nulla ac fermentum'
                    'urna. Nulla sed turpis ultricies, sollicitudin mi eu,'
                    'convallis ante. Proin ullamcorper enim eu est cras.'
                )
            )

    def test_should_create_author_without_last_name(self):
        Author.objects.create(name='Promoter')

        assert Author.objects.count() == 1
        assert Author.objects.get(name='Promoter').name == 'Promoter'


class TestBook:

    @pytest.fixture
    def create_author(self):
        Author.objects.create(name='Amaral', last_name='Macedo')
        return Author.objects.get(name='Amaral')

    def test_should_create_book(self, create_author):
        author = create_author
        book = Book.objects.create(
            name='Beasts',
            edition='1st',
            isbn='3b4bc5c0-fe08-4b1d-918d-5b3dc5dcfe22',
            publication_year=date.today()
        )
        book.authors.add(author)

        assert Book.objects.count() == 1
        assert book.name == 'Beasts'
        assert book.edition == '1st'
        assert book.isbn == '3b4bc5c0-fe08-4b1d-918d-5b3dc5dcfe22'
        assert book.publication_year == date.today()
        assert book.authors.get(name='Amaral') == author


