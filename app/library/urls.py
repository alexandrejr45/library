from django.contrib import admin
from django.urls import path, include
from library.core import views, urls

urlpatterns = [
    path('', include('library.core.urls')),
    path('admin/', admin.site.urls),
]
