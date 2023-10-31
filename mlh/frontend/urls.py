from django.urls import path
from . import views

#create the url
urlpatterns = [
    path('', views.home, name="home_page"),
    path('user/', views.user_form, name="user_page"),
    path('partner/', views.partner_form, name="partner_page"),
    path('redirectuser/', views.redirect_user, name="user_bio"),
    path('register/', views.register, name="register_page"),
    path('success/', views.success, name="success_page"),
    path('login/', views.login, name="login_page"),
]

