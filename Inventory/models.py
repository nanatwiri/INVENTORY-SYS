from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    description = models.TextField()
