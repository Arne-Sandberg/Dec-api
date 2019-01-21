from django.db import models

# Create your models here.
class Products(models.Model):
    """This class represents the Products model"""

    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=128)
    product_sport = models.CharField(max_length=128)
    product_level = models.PositiveIntegerField()
    product_description = models.TextField()
    associated_stores = models.ForeignKey('Stores',on_delete=models.CASCADE)

    def __str__(self):
        """string representation for products"""
        return self.product_name + " : " + self.product_sport


class Stores(models.Model):
    """This class represents the Stores model"""
    store_id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length=64)
    store_city = models.CharField(max_length=64)

    def __str__(self):
        return self.store_name

