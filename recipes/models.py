from __future__ import unicode_literals #Database can read all the languages
from django.db import models
from datetime import datetime

class FoodRecipes(models.Model):

    recipeName = models.CharField(u'Recipe name', help_text=u'The name of the recipe', max_length=30)

    def __str__(self):

        return self.recipeName


