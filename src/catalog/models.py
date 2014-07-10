#coding=utf8

from django.db import models
from django_extensions.db.models import TimeStampedModel


class Item(TimeStampedModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    email = models.EmailField(help_text=u'Только для получения анкет, не публикуется на сайте')
    salary = models.CharField(max_length=255, help_text=u'Фиксированная сумма или диапазон, может оставаться пустым')
    on_site = models.BooleanField(default=False)
    city = models.CharField(max_length=255, blank=True, null=True)
    employer_name = models.CharField(max_length=255, blank=True, null=True)
    employer_description = models.TextField(blank=True, null=True)
    employer_website = models.TextField(blank=True, null=True)

    class Meta:
        pass