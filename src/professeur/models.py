from django.db import models

# Create your models here.

class Professeur(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    city = models.CharField(max_length=100)
    birth_date = models.DateField()
    phone = models.CharField(max_length=10)
    is_vacant = models.BooleanField()
    matter = models.CharField(max_length=30)
    next_class = models.CharField(max_length=30)
    subject_next_meeting = models.CharField(max_length=100)
    