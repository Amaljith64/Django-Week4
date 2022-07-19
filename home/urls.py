from django import views
from django.conf import settings
from django.urls import path,include
from . import views

urlpatterns = [
     path('', views.index, name='home'),
     path('about/', views.about, name='about'),
     path('booking', views.book, name='book'),
     path('doctors', views.doctors, name='doctor'),
     path('contact', views.contact, name='contact'),
     path('departments', views.department, name='departments'),
] 