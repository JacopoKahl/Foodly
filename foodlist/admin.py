from django.contrib import admin
from .models import FoodList

#admin.site.register(FoodList)

# Personalization for the fields to be displayed in admin UI
@admin.register(FoodList)
class FoodAdmin(admin.ModelAdmin):
    fields = ['productName', 'productCategory', 'productExpDate', 'todayIs', 'productPrice']
    readonly_fields = ['todayIs'] # Prevent user modification to the today field
    #list_display = ['productName', 'productCategory', 'productExpDate', 'productStatus'] #display info in data tables



