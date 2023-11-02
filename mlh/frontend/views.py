from django.shortcuts import render, redirect
from backend.form import *
from .models import *
from django.http import HttpResponseBadRequest
from django.contrib.auth import authenticate, login 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def home(request) :
    return render(request, "html/home.html")

def success(request):
    return render(request, "html/success.html")

def user_form(request):
    if request.method == 'POST':
        form_user = UserInfoForm(request.POST)
        if form_user.is_valid():
            form_user.save()
            return redirect("user_bio")
    else:
        form_user = UserInfoForm()
    return render(request, 'html/user.html', {'form_user':form_user})

def partner_form(request):
    if request.method == 'POST':
        form_partner = PartnerInfoForm(request.POST)
        if form_partner.is_valid():
            form_partner.save()
            return redirect('html/partner.html')
    else:
        form_partner= PartnerInfoForm()
    return render(request, 'html/partner.html', {'form_partner':form_partner})

# for user

def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('login_user')
        messages.error(request, "Registration unsuccessful.")
    else:
        form = UserForm()
    return render(request, 'html/registeru.html', {'register_form': form})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None: 
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('user_page')
            else:
                messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()            
    return render(request, 'html/login.html', {'login_form': form})

# for partner

def register_partner(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('login_partner')
        messages.error(request, "Registration unsuccessful.")
    else:
        form = UserForm()
    return render(request, 'html/registerp.html', {'register_form': form})

def login_partner(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None: 
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('partner_page')
            else:
                messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()            
    return render(request, 'html/login.html', {'login_form': form})
