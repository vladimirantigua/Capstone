from django.shortcuts import render
from django.http import HttpResponse
# from .models import Inventory: need to be added to the admin.py and view.py
from .models import Inventory

# Create your views here.


def index(request):
    context = {
        'message': 'Count IT :) !'
    }
    return render(request, 'CountITapp/index.html', context)
