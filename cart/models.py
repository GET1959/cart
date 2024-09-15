from django.db import models

NULLABLE = {"null": True, "blank": True}


class CartItem(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_quantity = models.PositiveIntegerField()
    # total_price = models.DecimalField(
    #     max_digits=10,
    #     decimal_places=2,
    #     **NULLABLE
    # )
