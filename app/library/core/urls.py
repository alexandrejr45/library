from rest_framework.authtoken.views import obtain_auth_token

from django.urls import path
from library.core import views


urlpatterns = [
    path('authors/', views.AuthorCreate.as_view()),
    path('authors/<int:pk>', views.AuthorDetail.as_view()),
    path('books/', views.BookCreate.as_view()),
    path('books/<int:pk>', views.BookDetail.as_view()),
    path('get-token/', obtain_auth_token)
]
