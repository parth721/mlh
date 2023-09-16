from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=50)
    user_lon= models.IntegerField()
    user_lat = models.IntegerField()
    user_phone = models.IntegerField() #how to prepare the countrycode
    
    user_area = models.CharField(max_length=30)
    user_city = models.CharField(max_length=30)
    user_state = models.CharField(max_length=30)
    user_country = models.CharField(max_length=3)
    
    
    
class Partner(models.Model):
    partner_name = models.CharField(max_length=50)
    partner_lon = models.IntegerField()
    partner_lat = models.IntegerField()
    partner_phone = models.IntegerField()
    
    partner_area = models.CharField(max_length=30)
    partner_city = models.CharField(max_length=30)
    partner_state = models.CharField(max_length=30)
    partner_country = models.CharField(max_length=3)
    