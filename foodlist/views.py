from django.shortcuts import render, get_object_or_404, redirect
from .serializers import FoodSerializer, UserSerializer
from rest_framework.authentication import TokenAuthentication
from .models import FoodList
from recipes.models import FoodRecipes
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage


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

def panel(request):
    return render(request, 'backend/home.html')

def food_list(request):
    foods = FoodList.objects.all()

    return  render(request, 'backend/foodlist.html', {'foods':foods})

def food_add(request):

    if request.method == 'POST':
        productname = request.POST.get('productname')
        productcategory = request.POST.get('productcategory')
        expday = request.POST.get('expday')
        productprice = request.POST.get('productprice')
        #productnotes = request.POST.get('productnotes')

        if productname == "" or expday == "" or productprice == "":
            error = "All fields required"
            return render(request, 'backend/error.html', {'error': error})


        productimage = request.FILES['productimage']
        fst = FileSystemStorage()
        filename = fst.save(productimage.name, productimage)
        url = fst.url(filename)

        add = FoodList(productName=productname, productCategory=productcategory, productExpDate=expday, productPrice=productprice, productimage=url)
        add.save()
        return redirect('food_list')
    return  render(request, 'backend/foodlist_add.html')

class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

# class to pass objects model to trough REST API
class FoodViewset(viewsets.ModelViewSet):
    serializer_class = FoodSerializer
    queryset = FoodList.objects.all()

    #Activate in order to request Token access for users
    #authentication_classes = (TokenAuthentication,)