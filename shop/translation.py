from modeltranslation.translator import translator, TranslationOptions
from .models import ProductModel


class ProductModelTranslation(TranslationOptions):
    fields = ('title', 'short_description', 'long_description')

translator.register(ProductModel, ProductModelTranslation)