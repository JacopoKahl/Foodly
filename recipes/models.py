from __future__ import unicode_literals #Database can read all the languages
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from tinymce.models import HTMLField


class FoodRecipes(models.Model):

    STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )

    recipeName = models.CharField(u'Recipe name', help_text=u'The name of the recipe', max_length=30)
    imgRecipe = models.ImageField(upload_to='media', null=True)
    slug = models.SlugField(max_length = 250, unique_for_date='publish', default='-')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User', null=True)
    textRecipe = HTMLField(u'Recipe content', default='Get inspired')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):

        return self.recipeName
