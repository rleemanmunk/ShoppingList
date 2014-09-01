from django.contrib import admin
from GroceryItem.models import Category, Store, Item

class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,      {'fields': ['item_name', 'price']}),
        ('Item Information', {'fields': ['category', 'store']})
    ]
    list_filter = ['category', 'store']
    search_fields = ['item_name']

admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
admin.site.register(Store)
