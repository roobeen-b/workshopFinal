import imp
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('contact/', views.contact, name='contact')
]
