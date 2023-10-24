from django.shortcuts import render, redirect
from backend.form import *
from .models import *
from django.http import HttpResponse
from twilio.rest import Client
import random

# Create your views here.
def home(request) :
    return render(request, "html/home.html")

def user_form(request):
    if request.method == 'POST':
        form_user = UserFrom(request.POST)
        if form_user.is_valid():
            form_user.save()
            return redirect('html/user.html')
    else:
        form_user = UserForm()
    return render(request, 'html/user.html', {'form_user':form_user})

def partner_form(request):
    if request.method == 'POST':
        form_partner = PartnerForm(request.POST)
        if form_partner.is_valid():
            form_partner.save()
            return redirect('html/partner.html')
    else:
        form_partner= PartnerForm()
    return render(request, 'html/partner.html', {'form_partner':form_partner})

def redirect_user(request):
    if request.method == 'POST':
        bio_user = UserRef(request.POST)
        if bio_user.is_valid():
            bio_user.save()
            return redirect('html/user.html')
    else:
        bio_user = UserRef()
        
    return  render(request, 'html/userbio.html', {'bio_user':bio_user})
    
def redirect_partner(request):
    if request.method == 'POST':
        bio_partner = PartnerRef(request.POST)
        if bio_partner.is_valid():
            bio_partner.save()
            return redirect('html/partner.html')
    else:
        bio_partner = PartnerRef()
        
    return  render(request, 'html/partnerbio.html', {'bio_partner':bio_partner})
  
##### verification code  
'''  
def send_verification_code(phone_number):
    code = str(random.randint(1000,9999))
    client = Client("AC157a3deced6810930de61fcd331c090d", "22a173d4fad92dedf5ba699ca09fea7e")
    #client = Client()
    message = client.messages.create(to=["+91"+phone_number], from_="+15178360990", body=f'Your OTP is : {code}') 
    return code

def resendOTP(self):
        self.n = random.randint(1000,9999)
        self.client = Client("AC157a3deced6810930de61fcd331c090d", "22a173d4fad92dedf5ba699ca09fea7e")
        self.client.messages.create(to=["+91"+self.phone_number], from_="+15178360990", body=f'Your OTP is : {self.n}')
        

def verify_phone_number(request):
    if request.method == "POST":
        name = request.POST.get('name')
        country_code = request.POST.get('country_code')
        phone_number = request.POST.get('phone_number')

        #check existing user or not   
        user = User.objects.filter(phone_number = phone_number).first()
        if not user :
            user = User.objects.create(name = name, country_code = country_code, phone_number = phone_number )
            
        verification_code = send_verification_code(phone_number)
        
        request.session['verification_code'] = verification_code
        
        return redirect('enter_verification_code')
    return render(request, 'html/login.html')

def enter_verification_code(request):
    if request.method == "POST":
        entered_code = request.POST.get('code')
        saved_code = request.session.get('verification_code')
        if entered_code == saved_code :
            return render()                      #need some upgrade
        else:
            return redirect(request, 'html/login.html')       #need some upgrades     
'''
# redoing the verification with another system.
def login_view(request):
    return render(request, "login.html")

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        if Profile.objects.filter(phone_number = phone_number).exists():
            ...
        else:
            user = User.objects.create(username = username)
            profile = Profile.objects.create(user = user, phone_number = phone_number)
        
        return redirect('/')
    return render(request, 'register.html.')