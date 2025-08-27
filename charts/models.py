# charts/models.py

from django.db import models

class Product(models.Model):
    product_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    clicks = models.PositiveIntegerField()
    sales = models.PositiveIntegerField()
    click_sales_ratio = models.FloatField()
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    sales_price = models.DecimalField(max_digits=8, decimal_places=2)
    unit_profit = models.DecimalField(max_digits=8, decimal_places=2)
    total_profit = models.DecimalField(max_digits=10, decimal_places=2)
    profit_per_click = models.FloatField()

    def __str__(self):
        return f"{self.name} ({self.product_id})"
