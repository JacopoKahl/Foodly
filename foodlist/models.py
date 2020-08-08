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

class FoodList(models.Model):

    productName = models.CharField(u'Product name', help_text=u'The name of the product', max_length=100)
    productCategory = models.CharField(u'Product category', help_text=u'The type of food', max_length=10, choices=foodCategories, default='meat')
    productBuyDate = models.DateField(u'Buying day', help_text=u'When you bought it')
    productToday = models.DateTimeField(u'Today is', help_text=u'Today is', default=datetime.now, blank=True) #Check the actual day in order to compare the expiration date
    productExpDate = models.DateField(u'Expiring day', help_text=u'Food Expiration Dates')
    

    #productExpiredDays = "Product alredy Expired"
    #productNotExpired = "Product has not expired yet"
    '''
    if productToday < productExpDate:
        print (productNotExpired)
    else:
        print (productExpiredDays)
    '''

    def __str__(self):

        return self.productName + self.productCategory



