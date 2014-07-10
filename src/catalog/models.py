#coding=utf8

from django.db import models
from django_extensions.db.models import TimeStampedModel


class Item(TimeStampedModel):
    title = models.CharField(u'Название', max_length=255, help_text=u'Краткое описание вакансии')
    description = models.TextField(u'Полное описание')
    email = models.EmailField(u'Контактный E-mail', help_text=u'Только для получения анкет, не публикуется на сайте')
    salary = models.CharField(u'Заработная плата', max_length=255, help_text=u'Фиксированная сумма или диапазон, может оставаться пустым, не забывайте указывать знак валюты - это важно! ')
    on_site = models.BooleanField(u'Это работа только в офисе', default=False)
    city = models.CharField(u'Город', max_length=255, blank=True, null=True, help_text=u'В каком городе находится офис')
    employer_name = models.CharField(u'Название', max_length=255, blank=True, null=True, help_text=u'Название вашей компании или стартапа')
    employer_description = models.TextField(u'Описание', blank=True, null=True, help_text=u'Ваше краткое описание')
    employer_website = models.URLField(u'Сайт', blank=True, null=True, help_text=u'No SPAM')


    def __unicode__(self):
        return self.title

    class Meta:
        pass