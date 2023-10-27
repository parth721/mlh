from django.db import models
from multiselectfield import MultiSelectField
#from django.core.validators import RegexValidator

# Create your models here.
class UserInfo(models.Model):
    Name = models.CharField(max_length=20,)
    Phone = models.CharField(max_length = 10,) #validators=[RegexValidator(regrex = r'^[0-9]+$')])
    Country = models.CharField(max_length=2, choices=[('IN', 'India'), ('US', 'United States'), ('UK', 'United Kingdom')])
    
class UserBio(models.Model):
    Purpose = models.IntegerField(max_length=1, choices=[(1, 'Babycare'), (2, 'Cooking'),(3, 'Elderlycare'), (4, 'Others')])
    Area = models.CharField(max_length=15)
    City = models.CharField(max_length=15)
    State = models.CharField(max_length=15)
    user_lon= models.FloatField(max_length=10)
    user_lat = models.FloatField(max_length=10)
 
    
# creating database for partners   
    
    
class PartnerInfo(models.Model):
    partner_name = models.CharField(max_length=20)
    partner_phone = models.CharField(max_length = 10) #validators=[RegexValidator(regrex = r'^[0-9]+$')])
    partner_country = models.CharField(max_length=2, choices=[('IN', 'India'), ('US', 'United States'), ('UK', 'United Kingdom')])
     
class PartnerBio(models.Model):
    PURPOSE_CHOICES = (
        (1, 'Babycare'),
        (2, 'Cooking'),
        (3, 'Elderlycare'),
        (4, 'Others')
    )
    partner_purpose = MultiSelectField(choices=PURPOSE_CHOICES, max_choices=4, max_length=9) 
    partner_area = models.CharField(max_length=15)
    partner_city = models.CharField(max_length=15)
    partner_state = models.CharField(max_length=15)
    partner_lon = models.DecimalField(max_digits=4, decimal_places=4, default=0.0000)
    partner_lat = models.DecimalField(max_digits=4, decimal_places=4, default=0.0000)