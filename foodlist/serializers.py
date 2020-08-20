from rest_framework import serializers
from .models import FoodList

# Grab the objects model from the models in the app in order to pass them via REST API
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodList
        fields = ['id', 'productName', 'productCategory', 'productStatus', 'productExpDate', 'productBuyDate', 'productPrice']
