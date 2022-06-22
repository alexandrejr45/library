from rest_framework import viewsets, mixins, permissions
from rest_framework.authtoken.views import ObtainAuthToken

from .models import Author
from .serializers import AuthorSerializer


class AuthorView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        return super(AuthorView, self).create(request)

    def retrieve(self, request, *args, **kwargs):
        return super(AuthorView, self).retrieve(request)

    def destroy(self, request, *args, **kwargs):
        return super(AuthorView, self).destroy(request)

    def update(self, request, *args, **kwargs):
        return super(AuthorView, self).update(request)


class GetTokenView(ObtainAuthToken):
    pass
