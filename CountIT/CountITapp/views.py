from django.http import HttpResponse
# from .models import Inventory: need to be added to the admin.py and view.py
from .models import Inventory
from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect
# this is the Django built in user model: from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import InventoryForm
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.

# Paginator resource =  https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html
# we want the paginator to start on the home page which is the index page. this is why we put the paginator under the index view
# Create your views here.

# retrieve data from the database and pass it to the template


def index(request):
    # Order by quantity the items with less items at the top
    inventory_items = Inventory.objects.order_by('quantity')
    # Make a request to the page with GET because we are getting the page instead of post from the browser this is why is it is capital GET
    # page is one of the string objects and 1 is the page the page starts this is what is going to be display at the button of my page
    page = request.GET.get('page', 1)

    # paginator need to be done before the context variable below if do it after it will not show
    # create a variable and bring the model from line 6 Paginator
    # this will print 20 IT ITEMS per page
    paginator = Paginator(inventory_items, 15)
    # this is saying for every 15 IT_EQUIPMENT I need to create a new page
    inventory_items = paginator.page(page)

    # inventory_items = CountIT.objects.all().order_by('equipment_model')
    context = {
        'inventory_items': inventory_items
    }

    if request.method == "POST":
        query = request.POST['q']
        # print(type(query))
        # to void searching on empty field on the search bar do the following:
        if query:

            items = Inventory.objects.filter(
                Q(equipment_name__icontains=query)
                # icontain will eliminate any capitalization types__number__icontains
                | Q(equipment_model__icontains=query)
                | Q(asset_tag__icontains=query)
                | Q(service_tag__icontains=query)
                | Q(purchase_date__icontains=query)
                | Q(image_front__icontains=query)
                # icontain will eliminate any capitalization
                | Q(expiration_date__icontains=query)
                | Q(quantity__icontains=query))
            context['query'] = items

    return render(request, 'CountITapp/index.html', context)

# detail view


def detail(request, id):  # contact_id each person have a unique contact_id
    # I am searching by number
    # id=id get the inventory object whose id is the one I pass in the function
    item = get_object_or_404(Inventory, id=id)
    # IT_items = []  # make a list of just the types
    # for item in items.IT_items.all():
    #     # print(item)
    #     item.append(item.name)

    # {'contact': contact}) this is giving a single contact this is why is singular because when we click the name of one of the people in the contact list it will give only that person contact details instead of everyone else
    # to get a list of the types to turn the query set of the types into a list: list(IT_quipment.types.all())
    return render(request, 'CountITapp/search.html', {'item': item})

# https://docs.djangoproject.com/en/3.0/ref/request-response/
# https://stackoverflow.com/questions/38251922/logic-behind-formrequest-post-or-none

# add equipment view:


# @staticmethod
def add_equipment():
    form = InventoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('')
    context = {
        "form": form,
        # "name": addedEquipment
    }
    return render(request, "CountITapp/add_equipment.html", context)
# function will create a query set to in case I want to look for the items


# IT Items query search:


def search(query=None):
    queryset = []
    # this will do the search and divide the results with the coma
    queries = query.split(" ")
    # create a loop to search for the query:
    for q in queries:
        IT_items = Inventory.objects.filter(Q(types__name__icontains=q)
                                            # icontain will eliminate any capitalization types__number__icontains
                                            | Q(equipment_name__icontains=query)
                                            # icontain will eliminate any capitalization types__number__icontains
                                            | Q(equipment_model__icontains=query)
                                            | Q(asset_tag__icontains=query)
                                            | Q(service_tag__icontains=query)
                                            | Q(purchase_date__icontains=query)
                                            | Q(image_front__icontains=query)
                                            # icontain will eliminate any capitalization
                                            | Q(expiration_date__icontains=query)
                                            | Q(quantity__icontains=query))

    for IT_item in IT_items:  # to loop through each of the query
        queryset.append(IT_item)  # to add the to the query set
    # set will make sure the return is unique and then it is converted into a list that can be used in the template
    return list(set(queryset))


# @login_required requires that the users have to login and it will redirect to the login page to the page we set at the settings Login URLin to see the information on the site this is a decorator @login_required similar to the one we used in Flask
# if trying to go to the Home Page and you have not logged in yet it will
# redirect to this page which is the login page: http://localhost:8000/CountITapp/login/?next=/CountITapp/home/ for the user to enter username and pw and then redirect to the home page
@login_required
# Login page view
def home(request):
    # print(request.user.username)
    return render(request, 'CountITapp/home.html')

# login page view


def login_page(request):
    if request.method == 'POST':
        # to get the Username and Pw out of the form
        username = request.POST['username']
        password = request.POST['password']
        # if the user has been created the and the username and pw match you will be able to login:
        user = authenticate(request, username=username, password=password)
        # username and password do not match, go back to the page and didplay this message: {'message': 'Wrong User name and Password there is no user with this username and password. Please enter a valid Username and Password or click register to create an account'})
        if user is None:
            return render(request, 'CountITapp/login.html', {'message': 'Wrong Username and Password there is no user with this username and password. Please enter a valid Username and Password or click register to create an account'})
        # login(request, user) means if the user has been created then the user will be able to login and be redirected to the home page
        login(request, user)
        # if there's a next parameter in the url e.g. localhost:8000/CountITapp/login/?next=/CountITapp/home/
        if 'next' in request.GET:
            # redirect to next in this case is the login page
            return HttpResponseRedirect(request.GET['next'])
        return HttpResponseRedirect(reverse('CountITapp:home'))

    return render(request, 'CountITapp/login.html')

# register page view How to use my email as my username


def register_page(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        retype_password = request.POST['retype_password']
        # to check if the passwords are the same and to add a message such as: 'passwords do not match' when user register for an account do the following:
        if password != retype_password:
            return render(request, 'CountITapp/register.html', {'message': 'passwords do not match'})
        # check if a user with that username already exists
        if User.objects.filter(username=username).exists():
            # if User.objects.filter(email=email).exists():
            return render(request, 'CountITapp/register.html', {'message': 'Please use a different username the username you entered already exists'})
        # create the user, log them in, and redirect to the home page
        # this will create all the hashing and create the user -- user = User.objects.create_user(username, email, password)
        # if we want to utilize email as the username do it the format below by passing the username as the email (email, email, password)
        user = User.objects.create_user(email, email, password)
        login(request, user)
        # return HttpResponseRedirect(reverse('CountITapp:register'))
        # redirect to the homepage:
        return HttpResponseRedirect(reverse('CountITapp:home'))
    print(request.POST)
    return render(request, 'CountITapp/register.html')

# Logout view


def logout_user(request):
    logout(request)
    # after login out the user will be redirected to the login page:
    return HttpResponseRedirect(reverse('CountITapp:login_page'))


# def IT_items(request):
#     # Order by quantity the items with less items at the top
#     search = Inventory.objects.order.all()
#     # inventory_items = CountIT.objects.all().order_by('equipment_model')
#     context = {
#         'search': search
#     }
#     return render(request, 'IT_items/index.html', context)
