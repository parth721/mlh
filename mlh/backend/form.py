from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class UserForm(UserCreationForm):
    
    class Meta :
        model = User
        fields = ['username', 'password']
    
    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        if commit:
            user.save()
        return user
        
        
class UserInfoForm(forms.ModelForm):
    class Meta :
        model = UserInfo
        fields = [ 'First_name','Last_name','Purpose','Country','Phone', 'Area', 'City', 'State', 'Latitude','Longitude'] 
 
class PartnerInfoForm(forms.ModelForm):
    class Meta :
        model = PartnerInfo
        fields = ['First_name','Last_name','Purpose','Country','Phone', 'Area', 'City', 'State', 'Latitude','Longitude']