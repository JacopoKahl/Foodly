from __future__ import unicode_literals #Database can read all the languages
from django.db import models
from datetime import datetime

# Create your models here.

foodCategories = (
    ('meat','MEAT'),
    ('fruit', 'FRUIT'),
    ('vegetables','VEGETABLES'),
    ('fish','FISH'),
    ('pasta','PASTA'),
)

foodStatus = (
    ('good', 'GOOD'),
    ('expired', 'EXPIRED'),
)

#status = models.CharField(u'Product status', help_text=u'If the product is good to eat',max_length=7, choices=foodStatus, default='good')


class FoodList(models.Model):

    productName = models.CharField(u'Product name', help_text=u'The name of the product', max_length=100)
    productCategory = models.CharField(u'Product category', help_text=u'The type of food', max_length=10, choices=foodCategories, default='meat')
    productBuyDate = models.DateField(u'Buying day', help_text=u'When you bought it')
    productExpDate = models.DateField(u'Expiring day', help_text=u'Food Expiration Dates')

    todayIs = models.DateField(u'Today is', help_text=u'Check if the product is good to eat')
    #Had to be updated every day with a scheduled cron job

    def __str__(self):
        if self.todayIs >= self.productExpDate:
            self.status =  "expired"
        else:
            self.status =  "good"

        return self.productName + " " + self.productCategory + " " + self.status



