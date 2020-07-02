from django.http import HttpResponse
# from .models import Inventory: need to be added to the admin.py and view.py
from .models import Inventory
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


# retrieve data from the database and pass it to the template
def index(request):
    # Order by quantity the items with less items at the top
    inventory_items = Inventory.objects.order_by('quantity')
    # inventory_items = CountIT.objects.all().order_by('equipment_model')
    context = {
        'inventory_items': inventory_items
    }
    return render(request, 'CountITapp/index.html', context)


@login_required
def home(request):
    print(request.user.username)
    return render(request, 'CountITapp/home.html')


def login_page(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is None:  # username and password do not match, go back to the page
            return render(request, 'CountITapp/login.html', {'message': 'there is no user with that username and password'})
        # user was found, log them in and redirect to the home page
        login(request, user)
        # if there's a next parameter in the url e.g. localhost:8000/CountITapp/login/?next=/CountITapp/home/
        if 'next' in request.GET:
            return HttpResponseRedirect(request.GET['next'])
        return HttpResponseRedirect(reverse('CountITapp:home'))

    return render(request, 'CountITapp/login.html')


def register_page(request):
    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        retype_password = request.POST['retype_password']

        if password != retype_password:
            return render(request, 'CountITapp/register.html', {'message': 'passwords do not match'})
        # check if a user with that username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'CountITapp/register.html', {'message': 'username already exists'})
        # create the user, log them in, and redirect to the home page
        user = User.objects.create_user(username, email, password)
        login(request, user)
        return HttpResponseRedirect(reverse('CountITapp:home'))

    return render(request, 'CountITapp/register.html')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('CountITapp:login_page'))


# def IT_items(request):
#     # Order by quantity the items with less items at the top
#     search = Inventory.objects.order.all()
#     # inventory_items = CountIT.objects.all().order_by('equipment_model')
#     context = {
#         'search': search
#     }
#     return render(request, 'IT_items/index.html', context)

# if the user is not logged in, this redirects them to whatever path is in the settings.py as LOGIN_URL
# if the user is logged in, the view proceeds as usual
