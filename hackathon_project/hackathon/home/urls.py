from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
   path("",views.index,name='home'),
   path("about", views.about, name='about'),
   path("services", views.services, name='services'),
   path("contact", views.contact, name='contact'),
   path("service1", views.service1, name='service1'),
   path("service2", views.service2, name='service2'),
   path("service3", views.service3, name='service3'),
   path("service4", views.service4, name='service4'),
]
