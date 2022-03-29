from django.db import models


class Author(models.Model):
    name = models.CharField(null=False, max_length=200)
    last_name = models.CharField(null=True, max_length=100)


class Book(models.Model):
    name = models.CharField(null=False, max_length=500)
    edition = models.CharField(null=False, max_length=25)
    publication_year = models.DateField(null=True)
    isbn = models.CharField(null=False, unique=True, max_length=80)
    authors = models.ManyToManyField(Author)
