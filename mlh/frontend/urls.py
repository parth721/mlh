from django.urls import path

from . import views

#create the url
urlpatterns = [
    path("", views.home, name="home_page"),
    path("user", views.user, name="user_page"),
    path("partner", views.partner, name="partner_page"),
]