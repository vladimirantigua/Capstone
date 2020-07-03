from django.http import HttpResponse
# from .models import Inventory: need to be added to the admin.py and view.py
from .models import Inventory
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
    # this will print 20 pokemons per page
    paginator = Paginator(inventory_items, 15)
    # this is saying for every 15 pokemon I need to create a new page
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


def detail(request, id):  # contact_id each person have a unique contact_id
    # I am searching by number
    # id=id get the inventory object whose id is the one I pass in the function
    item = get_object_or_404(Inventory, id=id)
    # IT_items = []  # make a list of just the types
    # for item in items.IT_items.all():
    #     # print(item)
    #     item.append(item.name)

    # {'contact': contact}) this is giving a single contact this is why is singular because when we click the name of one of the people in the contact list it will give only that person contact details instead of everyone else
    # to get a list of the types to turn the query set of the types into a list: list(pokemon.types.all())
    return render(request, 'CountITapp/search.html', {'item': item})


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


# if the user is not logged in, this redirects them to whatever path is in the settings.py as LOGIN_URL
# if the user is logged in, the view proceeds as usual


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
