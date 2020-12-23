from django.contrib import admin
from myshoes.models import *

@admin.register(Matrial)
class MatrialAdmin(admin.ModelAdmin):
    list_display = ['matrial_num', 'matrial_name']
    search_filds = ['matrial_num']

@admin.register(Shoes)
class ShoesAdmin(admin.ModelAdmin):
    list_display = ['shoesnum', 'height','category_num','matrial_num','size']
    search_filds = ['shoesnum']


@admin.register(ShoesHeight)
class ShoesHeightAdmin(admin.ModelAdmin):
    list_display = ['height']
    search_filds = ['height']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_num', 'category_name']
    search_filds = ['category_num']
