from django.contrib import admin
from catalog.models import Item


class ItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(Item, ItemAdmin)