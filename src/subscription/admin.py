from django.contrib import admin
from models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email',]

admin.site.register(Subscription, SubscriptionAdmin)
