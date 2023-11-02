from django.urls import path
from . import views

#create the url
urlpatterns = [
    path('', views.home, name="home_page"),
    path('user/', views.user_form, name="user_page"),
    path('partner/', views.partner_form, name="partner_page"),
    path('registeru/', views.register_user, name="register_user"),
    path('registerp/', views.register_partner, name="register_partner"),
    path('success/', views.success, name="success_page"),
    path('loginu/', views.login_user, name="login_user"),
    path('loginp/', views.login_partner, name="login_partner"),
]

