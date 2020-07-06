from django.urls import path
from . import views

app_name = 'CountITapp'
urlpatterns = [
    # leave the path with empty quote void having to enter index path('', views.index, name='index')
    path('', views.index, name='index'),
    path('login/', views.login_page, name='login_page'),
    path('register/', views.register_page, name='register_page'),
    path('home/', views.home, name='home'),
    # path('', views.home, name='home'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('add_equipment/', views.add_equipment, name='add_equipment'),
    path('edit_equipment/<int:id>/', views.add_equipment, name='edit_equipment'),
    path('edit_equipment/submit/', views.edit_submit, name='edit_item_submit'),
    path('delete/<int:id>/', views.add_equipment, name='delete'),
    path('logout/', views.logout_user, name='logout_user'),
    path('search/', views.search, name='search'),

]
