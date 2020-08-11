from __future__ import unicode_literals #Database can read all the languages
from django.db import models
#from django.contrib.auth.models import User
from datetime import datetime

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class FoodRecipes(models.Model):

    recipeName = models.CharField(u'Recipe name', help_text=u'The name of the recipe', max_length=30)
    '''
    recipeSlug = models.SlugField(u'Recipe slug', help_text=u'The slug URL', max_length=200, default='your-url')
    #author = models.ForeignKey(u'Author', User, on_delete= models.CASCADE,related_name='blog_recipes', default='admin')
    recipeContent = models.TextField(u'Recipe content', help_text=u'Write here your recipe', default='Write here..')
    updated_on = models.DateField(u'Updated On')
    created_on = models.DateField(u'Created')
    recipeStatus = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']
    '''
    def __str__(self):

        return self.recipeName
