from django.shortcuts import render, redirect
from backend.form import *
from .models import *
from django.http import HttpResponseBadRequest
from django.contrib.auth import authenticate, login 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request) :
    return render(request, "html/home.html")

def success(request):
    return render(request, "html/success.html")

@login_required(login_url='login_user')
def user_form(request):
    user = request.user
    try:
        user_info = UserInfo.objects.get(user=user)
    except UserInfo.DoesNotExist:
        user_info = None
    if request.method == 'POST':
        if user_info is not None:
            form_user = UserInfoForm(request.POST, instance=user_info)
        else:
            form_user = UserInfoForm(request.POST)
        if form_user.is_valid():
            user_info = form_user.save(commit=False)
            user_info.user = request.user
            user_info.save()
            return redirect("success_page")
    else:
        if user_info is not None:
            form_user = UserInfoForm(instance=user_info)
        else:
            form_user = UserInfoForm()
    return render(request, 'html/user.html', {'form_user':form_user})


@login_required(login_url='login_partner')
def partner_form(request):
    if request.method == 'POST':
        form_partner = PartnerInfoForm(request.POST)
        if form_partner.is_valid():
            form_partner.save()
            
            # Retrieve userdata  
            country = form_partner.cleaned_data['Country']
            latitude = form_partner.cleaned_data['Latitude']
            longitude = form_partner.cleaned_data['Longitude']
            
            # query search 
            results = UserInfoForm.objects.filter(
                latitude__gte = latitude - 0.005,
                latitude__lte = latitude + 0.005,
                longitude__gte = longitude - 0.005,
                longitude__lte = longitude + 0.005,
            )
            results = results.filter(Country = country)
            
            return redirect('html/success.html', {'results' : results })
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