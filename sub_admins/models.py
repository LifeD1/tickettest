from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Agency(models.Model) :
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    reg_num = models.CharField(max_length = 100)
    signup_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name


class Branche(models.Model):
    name = models.CharField(max_length=100)
    town = models.CharField(max_length=100, null = True, blank= True)
    agency = models.ForeignKey(Agency, on_delete = (models.CASCADE))

    def __str__(self):
        return self.name




class User(AbstractUser):
    
    phone = models.CharField(max_length=50, null = True, blank =True)
    phone_2 = models.CharField(max_length=50, null = True, blank =True)
    id_card = models.CharField(max_length=100, null = True, blank= True)
    gender = models.CharField(
        max_length=6,
        choices = [('MALE', 'MALE'), ('FEMALE', 'FEMALE')],
        null = True,
        blank= True
    )
    agency = models.ForeignKey(Agency, on_delete = (models.CASCADE), null = True, blank= True)
    branch = models.ForeignKey(Branche, on_delete = (models.CASCADE), null = True, blank= True)


