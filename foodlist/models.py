from __future__ import unicode_literals #Database can read all the languages
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone
#from tagging_autocomplete_new.models import TagAutocompleteField

# Create your models here.


#status = models.CharField(u'Product status', help_text=u'If the product is good to eat',max_length=7, choices=foodStatus, default='good')


class FoodList(models.Model):
    foodCategories = (
        ('meat', 'MEAT'),
        ('fish', 'FISH'),
        ('fruit', 'FRUIT'),
        ('vegetables', 'VEGETABLES'),
        ('pasta', 'PASTA'),
        ('cheese', 'CHEESE'),
    )

    foodStatus = (
        ('good', 'GOOD'),
        ('expired', 'EXPIRED'),
    )

    productName = models.CharField(u'Product name', help_text=u'The name of the product', max_length=30)
    productStatus = models.CharField(u'Product status', max_length=10, choices=foodStatus, default='good')
    productCategory = models.CharField(u'Product category', help_text=u'The type of food', max_length=10, choices=foodCategories, default='meat')
    #productBuyDate = models.DateField(u'Buying day', help_text=u'When you bought it')
    productExpDate = models.DateField(u'Expiring day', help_text=u'Food Expiration Dates')
    todayIs = models.DateField(u'Today is', help_text=u'This will be helpful to calculate the expiration date', default=date.today,  blank=True)
    #Had to be updated every day with a scheduled cron job
    productPrice = models.DecimalField(u'Price', help_text=u'The price of the single product', max_digits=10, decimal_places=2)


    def __str__(self):
        today = date.today() #grab today date
        if today >= self.productExpDate:
            self.productStatus = 'expired'
        else:
            self.productStatus = 'good'

        self.save()

        return self.productName + " | " + self.productCategory + " | " + self.productStatus + " | " + str(
            self.productPrice) + "€"

