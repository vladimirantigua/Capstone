from django.urls import path
from . import views

app_name = 'CountITapp'
urlpatterns = [
    # leave the path with empty quote void having to enter index path('', views.index, name='index')
    path('', views.index, name='index')
]
