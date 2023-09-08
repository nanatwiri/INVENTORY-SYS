from django.db import models


class Suppliers(models.Model):
    SupplierID = models.AutoField(primary_key=True)
    SupplierName = models.CharField(max_length=255)

    def __str__(self):
        return self.SupplierName


class Products(models.Model):
    ProductID = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=255)
    SupplierID = models.ForeignKey(Suppliers, on_delete=models.CASCADE)
    UnitPrice = models.DecimalField(max_digits=10, decimal_places=2)
    Description = models.TextField()

    def __str__(self):
        return self.ProductName
