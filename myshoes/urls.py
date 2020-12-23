from django.urls import path, include, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('search/', views.search, name='search'),
]