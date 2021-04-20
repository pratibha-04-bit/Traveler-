from django.db import models
from datetime import datetime, date

# Create your models here.

class Travel_details(models.Model):
    place = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    address =  models.CharField(max_length=50)
    email =  models.EmailField(max_length=50)
    phone =  models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    from_date= models.DateField( auto_now = False)
    no_people = models.IntegerField()
    adult = models.IntegerField()
    children = models.IntegerField()
    class Meta:
      db_table="travel"