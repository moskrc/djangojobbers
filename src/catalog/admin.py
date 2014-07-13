from django.contrib import admin
from catalog.models import Item, Application


class ItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(Item, ItemAdmin)



class ApplicationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Application, ApplicationAdmin)