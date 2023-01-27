from django.shortcuts import get_object_or_404

from rest_framework import viewsets, mixins, permissions, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import generics


from library.core.models import Author, Book
from library.core.serializers import AuthorSerializer, BookSerializer


class AuthorView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
       return self.list(request, *args, **kwargs)
    def get_author(self, request, *args, **kwargs):
       return self.update(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class BookView(viewsets.ViewSet):

    def create(self, request):
        try:
            serializer = BookSerializer(data=request.data)

            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )

        except Exception as e:
            raise e

    def retrieve(self, request, pk=None):
        try:
            if pk:
                book = get_object_or_404(Book, isbn=pk)
                serializer = BookSerializer(book)
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK
                )
        except Exception as e:
            raise e

    def update(self, request, pk=None):
        try:
            if pk:
                book = get_object_or_404(Book, isbn=pk)
                serializer = BookSerializer(book, data=request.data)
                if serializer.is_valid(raise_exception=True):
                    return Response(
                        serializer.data,
                        status=status.HTTP_200_OK
                    )
        except Exception as e:
            raise e

    def destroy(self, request, pk=None):
        pass


class GetTokenView(ObtainAuthToken):
    pass
