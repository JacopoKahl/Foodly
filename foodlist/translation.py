'''
from modeltranslation.translator import translator, TranslationOptions
from .models import FoodList

class FoodListTranslationOptions(TranslationOptions):
    fields = ('productName', )

translator.register(FoodList, FoodListTranslationOptions)
'''