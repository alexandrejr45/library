import pytest
from library.core.serializers import (
    AuthorSerializer,
    BookSerializer
)
from rest_framework.exceptions import ValidationError

pytestmark = pytest.mark.django_db


class TestAuthorSerializer:

    def test_should_create_valid_author_serializer(
        self,
        author_payload_valid
    ):
        author_serializer = AuthorSerializer(data=author_payload_valid)

        assert author_serializer.is_valid() is True

    def test_should_raise_error_when_author_name_is_invalid(
        self,
        author_payload_invalid
    ):
        author_serializer = AuthorSerializer(data=author_payload_invalid)

        assert author_serializer.is_valid() is False


class TestBookSerializer:

    def test_should_create_valid_book_serializer(
        self,
        book_payload_valid
    ):
        book_serializer = BookSerializer(data=book_payload_valid)
        book_serializer.is_valid()

        assert book_serializer.is_valid() is True

    def test_should_raise_error_when_book_name_is_invalid(
        self,
        book_payload_invalid,
    ):
        with(pytest.raises(ValidationError)):
            book_serializer = BookSerializer(data=book_payload_invalid)
            book_serializer.is_valid(raise_exception=True)
