from datetime import datetime

from django.db import models


# Create your models here.
class Employer(models.Model):
    first_name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200 , blank=True)
    last_name = models.CharField(max_length=200)
    id_card = models.CharField(max_length=200 , blank=True)
    birthday = models.DateField(default=datetime.now)
    birthplace = models.CharField(max_length=50 , blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    hire_date = models.DateField()
    education = models.CharField(max_length=200 , blank=True)
    address = models.CharField(max_length=50 , blank=True)
    company_name = models.CharField(max_length=50 , blank=True)
    description = models.TextField(blank=True)


    def __str__(self):
        return self.first_name