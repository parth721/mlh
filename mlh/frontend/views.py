from django.shortcuts import render, redirect
from backend.form import UserForm
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
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = UserForm()
    return render(request, 'html/user.html', {'form':form})