from django.db import models
#from django.core.validators import RegexValidator

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=20)
    user_country = models.CharField(max_length=3)
    user_phone = models.CharField(max_length=10) #how to prepare the countrycode
 
class UserBio(models.Model):
    user_purpose = models.CharField(max_length=20)
    user_area = models.CharField(max_length=20)
    user_city = models.CharField(max_length=20)
    user_state = models.CharField(max_length=20)
    user_lon= models.DecimalField(max_digits=4, decimal_places=3, default=0.00)
    user_lat = models.DecimalField(max_digits=4,  decimal_places=3, default=0.00)
 
    
# creating database for partners   
    
    
class Partner(models.Model):
    partner_name = models.CharField(max_length=50)
    partner_country = models.CharField(max_length=3)
    partner_phone = models.CharField(max_length = 10) #validators=[RegexValidator(regrex = r'^[0-9]+$')])
    
     
class PartnerBio(models.Model):
    partner_area = models.CharField(max_length=30)
    partner_city = models.CharField(max_length=30)
    partner_state = models.CharField(max_length=30)
    partner_lon = models.DecimalField(max_digits=4, decimal_places=3, default=0.00)
    partner_lat = models.DecimalField(max_digits=4, decimal_places=3, default=0.00)