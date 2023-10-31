from django import forms
from .models import *


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta :
        model = User
        fields = ['username', 'email', 'password']
        
        
class UserInfoForm(forms.ModelForm):
    class Meta :
        model = UserInfo
        fields = [ 'Phone', 'Country'] 


class UserRef(forms.ModelForm):
    class Meta:
        model = UserBio
        fields = ['Purpose','Area', 'City', 'State', 'user_lat', 'user_lon']
     
class PartnerForm(forms.ModelForm):
    class Meta :
        model = PartnerInfo
        fields = ['partner_name', 'partner_phone', 'partner_country']
        

class PartnerRef(forms.ModelForm):
    class Meta:
        model = PartnerBio
        fields = ['partner_purpose', 'partner_area', 'partner_city', 'partner_state', 'partner_lat', 'partner_lon']  
     