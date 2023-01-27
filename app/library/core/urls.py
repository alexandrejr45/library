from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from django.urls import path, include
from library.core import views


router = DefaultRouter()
router.register(r'books', views.BookView, basename='books')

urlpatterns = [
    path('', include(router.urls)),
    path('authors/', views.AuthorView.as_view()),
    path('get-token/', obtain_auth_token)
]