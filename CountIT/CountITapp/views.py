from django.http import HttpResponse
# from .models import Inventory: need to be added to the admin.py and view.py
from .models import Inventory
from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect
# this is the Django built in user model: from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
import requests
# when add the recacha need to import the secret keys
from .import secrets


# Create your views here.

# Paginator resource =  https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html
# we want the paginator to start on the home page which is the index page. this is why we put the paginator under the index view
# Create your views here.

# retrieve data from the database and pass it to the template

# login_required
def index(request):
    # Order by quantity the items with less items at the top

    return render(request, 'CountITapp/index.html')

# detail view


def detail(request, id):  # IT_item_id each person have a unique IT_item_id
    # I am searching by number
    # id=id get the inventory object whose id is the one I pass in the function
    item = get_object_or_404(Inventory, id=id)
    # IT_items = []  # make a list of just the types
    # for item in items.IT_items.all():
    #     # print(item)
    #     item.append(item.name)
    context = {
        'item': item
    }

    # {'IT_item': IT_item}) this is giving a single IT_item this is why is singular because when we click the name of one of the people in the IT_item list it will give only that person IT_item details instead of everyone else
    # to get a list of the types to turn the query set of the types into a list: list(IT_quipment.types.all())
    # return render(request, 'CountITapp/edit.html', {'item': item})
    return render(request, 'CountITapp/detail.html', context)

# https://docs.djangoproject.com/en/3.0/ref/request-response/
# https://stackoverflow.com/questions/38251922/logic-behind-formrequest-post-or-none

# add equipment view:


def add_IT_equipment_page(request):
    return render(request, 'CountITapp/add_equipment.html', {})


def add_equipment(request):
    # When creating a new IT Equipment in the new add_IT_equipment_page it will show and create a field for the equipment name
    equipment_name = request.POST['equipment_name']
    equipment_model = request.POST['equipment_model']
    asset_tag = request.POST['asset_tag']
    service_tag = request.POST['service_tag']
    purchase_date = request.POST['purchase_date']
    # need to import from datetime import datetime. Also to parse the purchase and expiration
    purchase_date = datetime.strptime(purchase_date, '%Y-%m-%d').date()
    expiration_date = request.POST['expiration_date']
    expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d').date()
    quantity = request.POST['quantity']
    # in case I want to add an equipment image later:
    # image_front = request.POST['image_front']
    comments = request.POST['comments']

    # Create a tuple
    add_equipment = Inventory(equipment_name=equipment_name,
                              equipment_model=equipment_model,
                              asset_tag=asset_tag,
                              service_tag=service_tag,
                              purchase_date=purchase_date,
                              expiration_date=expiration_date,
                              quantity=quantity,
                              #   image_front=image_front,
                              comments=comments)
    add_equipment.save()  # to save IT_equipment to the database

    # remember to putting a comma at the end
    # redirecting to the detail page
    return HttpResponseRedirect(reverse('CountITapp:detail', args=(add_equipment.id,)))

# Delete IT_equipment:


def delete(request, id):
    inventory = Inventory.objects.get(id=id)
    inventory.delete()
    return HttpResponseRedirect(reverse('CountITapp:index'))

# edit IT_equipment combine submit and edit function:


def edit_equipment(request, id):
    inventory = get_object_or_404(Inventory, id=id)
    if request.method == "POST":
        print(request.POST)
        print(request.POST['purchase_date'])
        # When creating a new IT Equipment in the new add_IT_equipment_page it will show and create a field for the equipment name
        equipment_name = request.POST['equipment_name']
        equipment_model = request.POST['equipment_model']
        asset_tag = request.POST['asset_tag']
        service_tag = request.POST['service_tag']
        purchase_date = request.POST['purchase_date']
        # need to import from datetime import datetime. Also to parse the purchase and expiration
        purchase_date = datetime.strptime(purchase_date, '%Y-%m-%d').date()
        expiration_date = request.POST['expiration_date']
        expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d').date()
        quantity = request.POST['quantity']
        # in case I want to add an equipment image later:
        # image_front = request.POST['image_front']
        comments = request.POST['comments']

        # Getting the editing inventory:
        inventory = Inventory.objects.get(id=id)
        # assign values to the Inventory properties:
        inventory.equipment_name = equipment_name
        inventory.equipment_model = equipment_model
        inventory.asset_tag = asset_tag
        inventory.service_tag = service_tag
        inventory.purchase_date = purchase_date
        inventory.expiration_date = expiration_date
        inventory.quantity = quantity
        # in case I want to add an equipment image later:
        # inventory.image_front = image_front
        inventory.comments = comments

        inventory.save()  # to save IT_equipment to the database

        # remember to putting a comma at the end
        # redirecting to the detail page
        # if it is a POST request it will run everything inside the if statement above and return to the detail page
        return HttpResponseRedirect(reverse('CountITapp:detail', args=(inventory.id,)))

    context = {
        'item': inventory
    }
    # if it is a GET request will return to the edit equipment page so user can update the form
    return render(request, 'CountITapp/edit_equipment.html', context)


def edit_equipment_submit(request):
    print(request.POST)
    # When creating a new IT Equipment in the new add_IT_equipment_page it will show and create a field for the equipment name
    equipment_name = request.POST['equipment_name']
    equipment_model = request.POST['equipment_model']
    asset_tag = request.POST['asset_tag']
    service_tag = request.POST['service_tag']
    purchase_date = request.POST['purchase_date']
    # need to import from datetime import datetime. Also to parse the purchase and expiration
    purchase_date = datetime.strptime(purchase_date, '%Y-%m-%d').date()
    expiration_date = request.POST['expiration_date']
    expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d').date()
    quantity = request.POST['quantity']
    # in case I want to add an equipment image later:
    # image_front = request.POST['image_front']
    comments = request.POST['comments']

    # Getting the editing inventory:
    inventory = Inventory.objects.get(id=id)
    # assign values to the Inventory properties:
    inventory.equipment_name = equipment_name
    inventory.equipment_model = equipment_model
    inventory.asset_tag = asset_tag
    inventory.service_tag = service_tag
    inventory.purchase_date = purchase_date
    inventory.expiration_date = expiration_date
    inventory.quantity = quantity
    # in case I want to add an equipment image later:
    # inventory.image_front = image_front
    inventory.comments = comments

    inventory.save()  # to save IT_equipment to the database

    # remember to putting a comma at the end
    # redirecting to the detail page
    return HttpResponseRedirect(reverse('CountITapp:detail', args=(inventory.id,)))


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
                                            # in case I want to add an equipment image later and enable search:
                                            # | Q(image_front__icontains=query)
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
# @login_required
# Login page view
def equipment(request):
    # print(request.user.is_authenticated)
    if request.user.is_authenticated == False:
        # redirecting to the login page:
        return render(request, 'CountITapp/login.html')
    # inventory_items = Inventory.objects.all()
    inventory_items = Inventory.objects.order_by('quantity')
    context = {
        'items': inventory_items
    }
    # inventory_items = request.user.inventory_items.order_by('quantity')

    # Make a request to the page with GET because we are getting the page instead of post from the browser this is why is it is capital GET
    # page is one of the string objects and 1 is the page the page starts this is what is going to be display at the button of my page
    # page = request.GET.get('page', 1)

    # paginator need to be done before the context variable below if do it after it will not show
    # create a variable and bring the model from line 6 Paginator
    # this will print 20 IT ITEMS per page
    # paginator = Paginator(inventory_items, 15)
    # this is saying for every 15 IT_EQUIPMENT I need to create a new page
    # inventory_items = paginator.page(page)

    # inventory_items = CountIT.objects.all().order_by('equipment_model')

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
                # in case I want to add an image and how and be able to search it
                # | Q(image_front__icontains=query)
                # icontain will eliminate any capitalization
                | Q(expiration_date__icontains=query)
                | Q(quantity__icontains=query))
            context['query'] = items
            print(items)
    return render(request, 'CountITapp/equipment.html', context)

# login page view


def login_page(request):
    if request.method == 'POST':
        # make sure to alway print the form
        # print(request.POST)
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
        return HttpResponseRedirect(reverse('CountITapp:equipment'))

    return render(request, 'CountITapp/login.html')

# register page view How to use my email as my username


def register_page(request):

    if request.method == 'POST':
        # do the reCAPTCHA before submitting the form
        recaptcha_response = request.POST['g-recaptcha-response']
        # https://developers.google.com/recaptcha/docs/verify
        # https://www.w3schools.com/python/ref_requests_post.asp#:~:text=Python%20Requests%20post()%20Method&text=The%20post()%20method%20sends,some%20data%20to%20the%20server.
        response = requests.post('https://www.google.com/recaptcha/api/siteverify', data={
            'secret': secrets.recaptcha_secret_key,
            'response': recaptcha_response

        })
        recaptcha_response_data = response.json()
        if not recaptcha_response_data['success']:
            return render(request, 'CountITapp/register.html')
            # to add a message for the recaptcha see how can I add message for my register page and login page message = request.GET('message','')
            # return render(request, 'CountITapp/register.html', {'message':message})
            # return render(request, 'CountITapp/register.html')+'?message=invalid_recaptcha'
        # make sure to alway print the form
        # print(request.POST)
        # get th info out of the form
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        retype_password = request.POST['retype_password']
        # input validation on the backend - to check if the passwords are the same and to add a message such as: 'passwords do not match' when user register for an account do the following:
        if password != retype_password:
            return render(request, 'CountITapp/register.html', {'message': 'passwords do not match PW'})
        # check if a user with that username already exists
        if User.objects.filter(username=username).exists():
            # if User.objects.filter(email=email).exists():
            return render(request, 'CountITapp/register.html', {'message': 'Please use a different username the username you entered already exists'})
        # create the user, log them in, and redirect to the home page
        # this will create all the hashing and create the user -- user = User.objects.create_user(username, email, password)
        # if we want to utilize email as the username do it the format below by passing the username as the email (email, email, password)
        user = User.objects.create_user(username, email, password)
        login(request, user)
        # return HttpResponseRedirect(reverse('CountITapp:register'))
        # redirect to the homepage:
        return HttpResponseRedirect(reverse('CountITapp:equipment'))
    print(request.POST)
    return render(request, 'CountITapp/register.html')

# Logout view


def logout_user(request):
    logout(request)
    # after login out the user will be redirected to the login page:
    return HttpResponseRedirect(reverse('CountITapp:login_page'))

# profile page:


@login_required
def profile_page(request):

    print(request.user)
    print(request.user.email)
    if request.method == 'POST':
        # do the reCAPTCHA before submitting the form
        # recaptcha_response = request.POST['g-recaptcha-response']
        # # https://developers.google.com/recaptcha/docs/verify
        # # https://www.w3schools.com/python/ref_requests_post.asp#:~:text=Python%20Requests%20post()%20Method&text=The%20post()%20method%20sends,some%20data%20to%20the%20server.
        # response = requests.post('https://www.google.com/recaptcha/api/siteverify', data={
        #     'secret': secrets.recaptcha_secret_key,
        #     'response': recaptcha_response

        # })
        # recaptcha_response_data = response.json()
        # if not recaptcha_response_data['success']:
        #     return render(request, 'CountITapp/register.html')
        #     # to add a message for the recaptcha see how can I add message for my register page and login page message = request.GET('message','')
        #     # return render(request, 'CountITapp/register.html', {'message':message})
        #     # return render(request, 'CountITapp/register.html')+'?message=invalid_recaptcha'
        # # make sure to alway print the form
        # # print(request.POST)
        # # get th info out of the form

        # TO UPDATE THE EXISTING PROFILE do something like this below:
        # request.user.username = 'joe'
        # request.user.save()
        # request.user.password = ''
        # request.user.save()
        # request.user.email = ''
        # request.user.save()

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        retype_password = request.POST['retype_password']
        # input validation on the backend - to check if the passwords are the same and to add a message such as: 'passwords do not match' when user register for an account do the following:
        if password != retype_password:
            return render(request, 'CountITapp/register.html', {'message': 'passwords do not match'})
        # check if a user with that username already exists
        if User.objects.filter(username=username).exists():
            # if User.objects.filter(email=email).exists():
            return render(request, 'CountITapp/register.html', {'message': 'Please use a different username the username you entered already exists'})
        # create the user, log them in, and redirect to the home page
        # this will create all the hashing and create the user -- user = User.objects.create_user(username, email, password)
        # if we want to utilize email as the username do it the format below by passing the username as the email (email, email, password)
        user = User.objects.create_user(username, email, password)
        login(request, user)
        # return HttpResponseRedirect(reverse('CountITapp:register'))
        # redirect to the homepage:
        return HttpResponseRedirect(reverse('CountITapp:equipment'))
    print(request.POST)
    context = {
        'user': request.user
    }
    return render(request, 'CountITapp/profile_page.html')
