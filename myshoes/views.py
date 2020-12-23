import operator
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView
from django.contrib.auth.forms import UserChangeForm
from django.core.exceptions import ObjectDoesNotExist
from .forms import ShoesForm
from django.contrib import messages
from django.db.models import Q



def index(request):
    shoes = Shoes.objects.all()
    return render(request, 'myshoes/index.html',{'shoes':shoes })

def search(request):
    shoes = Shoes.objects.all()

    height = request.GET.get('height', '')
    matrial_num = request.GET.get('matrial_num', '')

    if height:
        shoes = shoes.filter(Q(height__height__icontains=height))
        shoes = shoes.filter(Q(matrial_num__matrial_num__icontains=matrial_num))

        return render(request, 'myshoes/index.html', {'shoes' : shoes})
    
    else:
        return render(request, 'myshoes/index.html')




