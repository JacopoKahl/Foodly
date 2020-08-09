from django.shortcuts import render, get_object_or_404, redirect
from .models import FoodList

# Create your views here.

def home(request):

    siteName = "Foodly"

    return render(request, 'frontend/home.html', {'siteName':siteName})

def features(request):

    siteName = "Foodly"

    return render(request, 'frontend/features.html', {'siteName':siteName})