from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from django.urls import path, include
from library.core import views


router = DefaultRouter()
router.register(r'authors', views.AuthorView, basename='authors')

urlpatterns = [
    path('', include(router.urls)),
    path('get-token/', obtain_auth_token)
]
