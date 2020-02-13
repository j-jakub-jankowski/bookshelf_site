from django.core.exceptions import ValidationError
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=200)
    published_date = models.IntegerField()
    isbn = models.CharField(max_length=20, null=True)
    page_count = models.IntegerField(null=True)
    small_thumbnail = models.URLField(null=True)
    language = models.CharField(max_length=3)

    def clean(self):
        if self.published_date < 1452:
            raise ValidationError('The first book was created in 1452')
        if self.published_date > 2021:
            raise ValidationError('Incorrect date')
        if self.page_count < 1:
            raise ValidationError('Incorrect page count, choose from range 1-10000')
