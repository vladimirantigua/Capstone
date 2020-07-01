from django.contrib import admin
from .forms import InventoryForm
from .models import Inventory

# Register your models here.

# if I want to add more things to display on my forms include it to the display list below:


class InventoryAdmin(admin.ModelAdmin):
    list_display = ['equipment_name', 'equipment_model',
                    'asset_tag', 'service_tag', 'quantity']
    form = InventoryForm
    filter = ['equipment_model']
    search = ['equipment_name', 'equipment_model']


admin.site.register(Inventory, InventoryAdmin)
