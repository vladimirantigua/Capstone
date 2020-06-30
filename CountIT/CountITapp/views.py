from django.shortcuts import render
from django.http import HttpResponse
# from .models import Inventory: need to be added to the admin.py and view.py
from .models import Inventory

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
