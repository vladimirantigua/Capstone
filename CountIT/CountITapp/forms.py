from django import forms
from .models import Inventory

# the import above we tight the models.py and forms
# this will allow the IT Team to update the inventory from the page instead of the admin panel

# create the form model below:
# https://tutorial.djangogirls.org/en/django_forms/
# https://www.youtube.com/watch?v=6oOHlcHkX2U


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['equipment_name', 'equipment_model',
                  'asset_tag', 'service_tag', 'purchase_date', 'expiration_date', 'quantity']
