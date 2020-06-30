from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    context = {
        'message': 'Count IT :) !'
    }
    return render(request, 'CountITapp/index.html', context)
