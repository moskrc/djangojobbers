#coding=utf8
from django.db import models
from django_extensions.db.models import TimeStampedModel


class Subscription(TimeStampedModel):
    name = models.CharField(u'Имя', max_length=255, help_text=u'На имя кого отправлять почту')
    email = models.EmailField(u'Контактный E-mail', help_text=u'Адрес для получения новых вакансий')


    def __unicode__(self):
        return self.name

    class Meta:
        pass

