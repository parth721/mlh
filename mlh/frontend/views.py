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
    