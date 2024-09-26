
from django.contrib import admin
from django.urls import path
from .views import all_chai

urlpatterns = [
    path('', all_chai,name="all_home"),
    # path('order/', views.all_chai,name="order"),
    
   
]
