from django.shortcuts import render, redirect
from backend.form import *
from .models import *
from django.http import HttpResponse
from twilio.rest import Client
import random

# Create your views here.
def home(request) :
    return render(request, "html/home.html")

def success(request):
    return render(request, "html/success.html")

def user_form(request):
    if request.method == 'POST':
        form_user = UserForm(request.POST)
        if form_user.is_valid():
            form_user.save()
            return redirect("login_page")
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


def login(request):
    return render(request, "html/login.html")

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

# the verification with another system.
def sendOTP(phone_number, request):
    otp = str(random.randrange(1000, 9999))
    client = Client("AC157a3deced6810930de61fcd331c090d", "22a173d4fad92dedf5ba699ca09fea7e")
    client.messages.create(to=["+91" + phone_number], from_="+15178360990", body=f'Your OTP is : {otp}')
    request.session['verification_code'] = otp

def resendOTP(phone_number, request):
    newotp = random.randrange(1000, 9999)
    client = Client("AC157a3deced6810930de61fcd331c090d", "22a173d4fad92dedf5ba699ca09fea7e")
    client.messages.create(to=["+91" + phone_number], from_="+15178360990", body=f'Your new OTP is : {newotp}')
    request.session['verification_code'] = newotp

def verify_phone_number(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('code')
        saved_otp = request.session.get('verification_code')

        # Check if the OTP is valid.
        if entered_otp != saved_otp:
            return render(request, 'html/user.html', {'error_message': 'Invalid OTP.'})

        # The OTP is valid
        form_user = UserForm(request.POST)

        if form_user.is_valid():
            form_user.save()
            return redirect('success_page')
        else:
            return render(request, 'html/user.html', {'form_user': form_user, 'error_message': 'Invalid user information.'})
    else:
        form_user = UserForm()
        return render(request, 'html/user.html', {'form_user': form_user})
