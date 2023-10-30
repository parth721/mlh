from django.urls import path
from . import views

#create the url
urlpatterns = [
    path('', views.home, name="home_page"),
    path('user/', views.user_form, name="user_page"),
    path('partner/', views.partner_form, name="partner_page"),
    path('redirectuser/', views.create_user_bio, name="user_bio"),
    path('redirectpartner/', views.redirect_partner, name="partner_bio"),
    path('success/', views.success, name="success_page"),
    path('login/', views.login, name="login_page"),
    path('create_user_info/', views.create_user_info, name='create_user_info'),
    path('create_user_bio/<int:user_id>/', views.create_user_bio, name='create_user_bio'),
    path('success_page/', views.success_page, name='success_page'),
]

