from django.db import models
from agencies.models import Bus
from sub_admins.models import Agency, Branche, User

# Create your models here.
class Reservation(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    customer = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    first_name = models.CharField(max_length = 100, null=True)
    last_name = models.CharField(max_length = 100, null=True)
    id_card = models.CharField(max_length = 100, null=True)
    phone = models.CharField(max_length = 100, null=True)
    bus = models.ForeignKey(Bus, on_delete = models.SET_NULL, null=True)
    agency = models.ForeignKey(Agency, on_delete= models.SET_NULL, null=True)
    branch = models.ForeignKey(Branche, on_delete= models.SET_NULL, null=True)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100, null=True, blank=True )
    departure_time = models.DateTimeField()
    trip_type = models.CharField(max_length=50)
    bus_type = models.CharField(max_length=50)
    number_of_persons = models.CharField(max_length=50)
    seat_number = models.CharField(max_length=10)
    trip_cost = models.CharField(max_length=50) 

    # def __str__(self):
    #      return self.customer