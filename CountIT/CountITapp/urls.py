from django.urls import path
from . import views

app_name = 'CountITapp'
urlpatterns = [
    # leave the path with empty quote void having to enter index path('', views.index, name='index')
    path('', views.index, name='index'),
    path('login/', views.login_page, name='login_page'),
    path('register/', views.register_page, name='register_page'),
    path('home/', views.home, name='home'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('logout/', views.logout_user, name='logout_user'),
]
path('<int:pokemon_id>/', views.detail, name='detail')
