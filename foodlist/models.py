from __future__ import unicode_literals #Database can read all the languages
from django.db import models

# Create your models here.

class FoodList(models.Model):

    productName = models.TextField()
    productCategory = models.TextField()
    productBuyDate = models.DateField()
    productExpDate = models.DateField()

    def __str__(self):
        return self.productName + self.productCategory

