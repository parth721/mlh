from django.shortcuts import render

# Create your views here.
def home(request) :
    return render(request, "html/home.html")

def user(request) :
    return render(request, "html/user.html")

def partner(request, name) :
    return render(request, "html/partner.html", {
        "name":name.capitalize()
    })