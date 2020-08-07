from django.shortcuts import render, get_object_or_404, redirect
from .models import FoodList

# Create your views here.

def home(request):

    return render(request, 'frontend/home.html')

def features(request):

    return render(request, 'frontend/features.html')