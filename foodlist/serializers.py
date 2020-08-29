from rest_framework import serializers
from django.contrib.auth.models import User
from .models import FoodList
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        user = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

# Grab the objects model from the models in the app in order to pass them via REST API
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodList
        fields = ('id', 'productName', 'productCategory', 'productStatus', 'productExpDate', 'productPrice')