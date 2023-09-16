from django.shortcuts import render, redirect
from backend.models import User
from backend.form import UserForm

# Create your views here.
def create_record(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = UserForm()
    return render(request, 'html/user.html', {'form': form})


class Geocoding :
    def Geocoding (self, request):
       area = request.area
       city = request.city
       state = request.state
       country = request.country
       # for url-encoded palce use urllib.parse
       ... 

class Geosearch :
    # looking for 
    ...