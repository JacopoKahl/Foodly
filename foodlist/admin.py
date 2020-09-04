from django.contrib import admin
from .models import FoodList
#FamilyList

#admin.site.register(FoodList)

# Personalization for the fields to be displayed in admin UI
@admin.register(FoodList)
class FoodAdmin(admin.ModelAdmin):
    fields = ['productName', 'productCategory', 'productExpDate', 'todayIs', 'productPrice', 'productImg']
    readonly_fields = ['todayIs'] # Prevent user modification to the today field
    #list_display = ['productName', 'productCategory', 'productExpDate', 'productStatus'] #display info in data tables


#admin.site.register(FamilyList)
#class FamilyFood(admin.ModelAdmin):
#    fields = ['lists', 'user', 'quantity']
