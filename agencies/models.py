from django.db import models
from sub_admins.models import Agency, Branche

# from sub_admins.models import Agency

# Create your models here.
class Bus_layout(models.Model):
    layout = models.CharField(max_length=100)
    num_seats = models.CharField(max_length=100)

    def __str__(self):
        return self.layout


class Bus(models.Model):
    bus_layout = models.ForeignKey(Bus_layout, on_delete = (models.CASCADE))
    agency = models.ForeignKey(Agency, on_delete = (models.CASCADE))
    bus_type = models.CharField(max_length=100)
    bus_number = models.CharField(max_length = 100)
    numb_seats = models.CharField(max_length=100)

    def __str__(self):
        return self.bus_number
    

class Driver(models.Model):
    agency = models.ForeignKey(Agency, on_delete = (models.CASCADE))
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=6,
        choices = [('MALE', 'MALE'), ('FEMALE', 'FEMALE')],
        null = True,
        blank= True
    )
    id_card = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name


class Trip(models.Model):
    trip_id = models.AutoField(primary_key=True)
    bus = models.ForeignKey(Bus, on_delete=models.SET_NULL, null=True)
    driver_id = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)
    agency = models.ForeignKey(Agency, on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(Branche, on_delete=models.SET_NULL, null=True)
    from_origin = models.CharField(max_length=150)
    to_destination = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True) 
    departure_time = models.DateTimeField()  #to be set by admin need to remove auto now add
    arrival_time = models.DateTimeField() #to be set by admin need to remove auto now add
    trip_cost = models.CharField(max_length=20)
    bus_type = models.CharField(max_length=20)