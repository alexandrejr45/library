import pytest
from library.core.serializers import (
    AuthorSerializer
)

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
