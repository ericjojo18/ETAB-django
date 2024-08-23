from django.db import models

# Create your models here.
class Eleve(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    city = models.CharField(max_length=100)
    birth_date = models.DateField()
    phone = models.CharField(max_length=10)
    classrom = models.CharField(max_length=10)
    registration_number = models.CharField(max_length=30)
    
    