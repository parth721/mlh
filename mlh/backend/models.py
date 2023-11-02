from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    First_name = models.CharField(max_length=10, blank=False)
    Last_name = models.CharField(max_length=10, blank=False)
    Purpose = models.IntegerField( blank=False, choices=[(1, 'Babycare'), (2, 'Cooking'),(3, 'Elderlycare'), (4, 'Others')])
    Country = models.CharField(max_length=2, blank=False, choices=[('IN', 'India'), ('US', 'United States'), ('UK', 'United Kingdom')])
    Phone = models.CharField(max_length = 10, blank=False) #validators=[RegexValidator(regrex = r'^[0-9]+$')])
    Area = models.CharField(max_length=10, blank=True)
    City = models.CharField(max_length=10, blank=True)
    State = models.CharField(max_length=10, blank=True)
    Latitude= models.FloatField(blank=False)
    Longitude = models.FloatField(blank=False)
 
    
# creating database for partners     
class PartnerInfo(models.Model):
    PURPOSE_CHOICES = (
        (1, 'Babycare'),
        (2, 'Cooking'),
        (3, 'Elderlycare'),
        (4, 'Others')
    )
    partner = models.OneToOneField(User, on_delete=models.CASCADE)
    Purpose = MultiSelectField(choices=PURPOSE_CHOICES, max_choices=4, max_length=9)
    First_name = models.CharField(max_length=10, blank=False)
    Last_name = models.CharField(max_length=10, blank=False)
    Country = models.CharField(max_length=2, choices=[('IN', 'India'), ('US', 'United States'), ('UK', 'United Kingdom')])
    Phone = models.CharField(max_length = 10, blank=False) #validators=[RegexValidator(regrex = r'^[0-9]+$')])
    Area = models.CharField(max_length=10, blank=True)
    City = models.CharField(max_length=10, blank=True)
    State = models.CharField(max_length=10, blank=True)
    Longitude = models.FloatField(blank=False)
    Latitude = models.FloatField(blank=False)
    