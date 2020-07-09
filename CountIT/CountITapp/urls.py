from django.urls import path
from . import views

app_name = 'CountITapp'
urlpatterns = [
    # leave the path with empty quote void having to enter index path('', views.index, name='index')
    path('', views.index, name='index'),
    path('login/', views.login_page, name='login_page'),
    path('register/', views.register_page, name='register_page'),
    path('profile_page/', views.profile_page, name='profile_page'),

    # path('home/', views.home, name='home'),
    # list inventory items on 'equipment' page have search there too
    path('equipment/', views.equipment, name='equipment'),
    # path('', views.home, name='home'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('add_equipment/', views.add_IT_equipment_page, name='add_equipment'),
    path('add_equipment_post/', views.add_equipment, name='add_equipment_post'),
    path('edit_equipment/<int:id>/', views.edit_equipment, name='edit_equipment'),
    path('edit_equipment/submit/',
         views.edit_equipment_submit, name='edit_item_submit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('logout/', views.logout_user, name='logout_user'),
    path('search/', views.search, name='search'),


]
