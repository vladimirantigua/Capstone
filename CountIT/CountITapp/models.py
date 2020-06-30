from django.db import models


# Create your models here.


class Inventory(models.Model):
    # equipment_name = Dell Latitude 15-inch laptop or Latitude 13-inch travel laptop or Microsoft Surface or  Dell OptiPlex Desktop Precision 5530
    equipment_name = models.CharField(max_length=200, null=True, blank=True)
    # equipment_model = 5590 (15' laptop high performace laptop 16GB Ram) or 7390(13' laptop for travel)
    equipment_model = models.CharField(max_length=200, null=True, blank=True)
    # asset_tags used for accounting and finance L = laptop D = destop P = Precision Engineer laptops 32GB Ram
    asset_tag = models.CharField(max_length=200, null=True, blank=True)
    # service tags = L15w10a L=laptop 15 means 15 inches w10 = windows 10 a = means a random letter I assigned to make it unique  used for IT department to utilize the Dell warranty and services and to apply the correct software updates according the service tags from Dell
    service_tag = models.CharField(max_length=200, null=True, blank=True)
    # purchase_date = will help with the expiration date will help scheduling with the recycling and refreshing timely and for accounting and finance to clear this assets from the books
    purchase_date = models.DateTimeField(null=True, blank=True)
    # expiration_date = laptops will be refreshed every 4 years according to the IT policy
    expiration_date = models.DateTimeField(null=True, blank=True)
    # quantity = will help mantain proper level of equipment on stock for each of the four quarters during the physical year
    quantity = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.equipment_name + ' - ' + self.equipment_model + ' - ' + self.quantity

# check with the Matthew or TAs to see if my models are correct
# see if I need to create a users models login or if I can use the build in Django user login check if need to create a user login pw if using the built in user that was created
