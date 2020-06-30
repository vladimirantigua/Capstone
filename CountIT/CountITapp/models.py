from django.db import models

# Create your models here.


class Inventory(models.Model):
    equipment_name = models.CharField(max_length=200)
    equipment_model = models.CharField(max_length=200)
    purchase_date = models.DateTimeField()
    expiration_date = models.DateTimeField()
    quantity = models.IntegerField(default='0')

    def __str__(self):
        return self.equipment_name + ' - ' + self.equipment_model + ' - ' + self.quantity

# check with the Matthew or TAs to see if my models are correct
# see if I need to create a users models login or if I can use the build in Django user login check if need to create a user login pw if using the built in user that was created
