from django.db import models


class Author(models.Model):
    name = models.CharField(null=False, max_length=300)


class Book(models.Model):
    name = models.CharField(null=False, max_length=500)
    edition = models.CharField(null=False, max_length=25)
    publication_year = models.DateField(null=True)
    authors = models.ManyToManyField(Author)
