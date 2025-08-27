from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'name', 'clicks', 'sales', 'total_profit', 'profit_per_click')
    search_fields = ('name',)