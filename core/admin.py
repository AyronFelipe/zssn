from django.contrib import admin
from .models import Sobrevivente, Inventario, Item


class SobreviventeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Sobrevivente, SobreviventeAdmin)


class InventarioAdmin(admin.ModelAdmin):
    pass
admin.site.register(Inventario, InventarioAdmin)


class ItemAdmin(admin.ModelAdmin):
    pass
admin.site.register(Item, ItemAdmin)
