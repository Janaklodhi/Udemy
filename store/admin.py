from django.contrib import admin
from store.models import Product, Category



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'description', 'image')  # Fields to display in list view
    list_filter = ('category',)  # Optionally, you can add category filtering
    search_fields = ('name', 'category__name')  # M


admin.site.register(Product)
admin.site.register(Category)