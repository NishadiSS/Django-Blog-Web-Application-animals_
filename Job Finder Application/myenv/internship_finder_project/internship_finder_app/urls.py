from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('enter_internship', views.enter_internship, name='enter_internship'),
    path('search_internship', views.search_internship, name='search_internship'),
    path('enter_information', views.enter_information, name='enter_information'),



]