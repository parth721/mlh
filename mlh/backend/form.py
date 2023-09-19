from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta :
        model = User
        fields = ['user_name', 'user_country', 'user_phone']

class UserRef(forms.ModelForm):
    class Meta:
        model = UserBio
        fields = ['user_purpose','user_area', 'user_city', 'user_state', 'user_lat', 'user_lon']
        
class PartnerForm(forms.ModelForm):
    class Meta :
        model = Partner
        fields = ['partner_name', 'partner_country', 'partner_phone']

class PartnerRef(forms.ModelForm):
    class Meta:
        model = PartnerBio
        fields = ['partner_area', 'partner_city', 'partner_state', 'partner_lat', 'partner_lon']        