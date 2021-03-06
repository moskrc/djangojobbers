# -*- coding: utf-8 -*-
import os
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.core.management.base import NoArgsCommand

from django.template.loader import render_to_string
from django.utils.html import strip_tags
from catalog.models import Item
from subscription.models import Subscription


class Command(NoArgsCommand):
    help = u"Send Emails"

    def handle(self, *args, **options):

        for i in Item.objects.filter(not_sended=True):
            for s in Subscription.objects.filter(site=i.site):
                print 'Send %s to %s' % (i, s)
                c = {
                    'site': i.site,
                    'item': i,
                }

                subject = render_to_string('catalog/email/new_item_subject.txt', c)
                html_body = render_to_string('catalog/email/new_item_body.html', c)
                text_body = strip_tags(html_body)

                msg = EmailMultiAlternatives(subject, text_body, None, s.email.split(','))
                msg.attach_alternative(html_body, "text/html")
                msg.send()

            i.not_sended=False
            i.save()

