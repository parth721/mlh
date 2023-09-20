from django.shortcuts import render, redirect
from backend.form import *
# to send http resonse from views file we added django.http
from django.http import HttpResponse

# Create your views here.
def home(request) :
    return render(request, "html/home.html")

def user(request) :
    return render(request, "html/user.html")

def partner(request) :
    return render(request, "html/partner.html")

def user_form(request):
    if request.method == 'POST':
        form_user = UserForm(request.POST)
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
    response = redirect('html/userbio.html')
    return response
    
def redirect_partner(request):
    response = redirect('html/partnerbio.html')
    return response
    