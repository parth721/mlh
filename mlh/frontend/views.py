from django.shortcuts import render
# to send http resonse from views file we added django.http
from django.http import HttpResponse

# Create your views here.
def home(request) :
    return render(request, "html/home.html")

def user(request) :
    return render(request, "html/user.html")

def partner(request) :
    return render(request, "html/partner.html")