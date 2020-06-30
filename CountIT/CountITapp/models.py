from django.db import models


# Create your models here.


class Inventory(models.Model):
    equipment_name = models.CharField(max_length=200, null=True, blank=True)
    equipment_model = models.CharField(max_length=200, null=True, blank=True)
    # asset_tags used for accounting and finance
    asset_tag = models.CharField(max_length=200, null=True, blank=True)
    # service tags used for IT department to utilize the Dell warranty and services and to apply the correct software updates according the service tags from Dell
    service_tag = models.CharField(max_length=200, null=True, blank=True)
    purchase_date = models.DateTimeField(null=True, blank=True)
    expiration_date = models.DateTimeField(null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.equipment_name + ' - ' + self.equipment_model + ' - ' + self.quantity

# check with the Matthew or TAs to see if my models are correct
# see if I need to create a users models login or if I can use the build in Django user login check if need to create a user login pw if using the built in user that was created
