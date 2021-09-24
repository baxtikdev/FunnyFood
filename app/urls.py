from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('team/',team,name='team'),
    path('about_product/<int:id>/',about_product,name='about_product'),
    path('menu/',menu,name='menu'),
    path('about/',about,name='about'),
    path('login/',login,name='login'),
]