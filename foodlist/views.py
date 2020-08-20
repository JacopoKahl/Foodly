from django.shortcuts import render, get_object_or_404, redirect
from .models import FoodList
from recipes.models import FoodRecipes
from rest_framework import viewsets
from .serializers import FoodSerializer
from rest_framework.authentication import TokenAuthentication

# Create your views here.

def home(request):

    siteName = "Foodly"
    

    return render(request, 'frontend/home.html', {'siteName':siteName})

def features(request):

    siteName = "Foodly"

    return render(request, 'frontend/features.html', {'siteName':siteName})

def recipes(request):

    siteName = "Foodly"
    recipes = FoodRecipes.objects.all()
    return render(request, 'frontend/recipes.html', {'siteName':siteName, 'recipes':recipes})

# class to pass objects model to trough REST API
class FoodViewset(viewsets.ModelViewSet):
    serializer_class = FoodSerializer
    queryset = FoodList.objects.all()
    authentication_classes = (TokenAuthentication,)