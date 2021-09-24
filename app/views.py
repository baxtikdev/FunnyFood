from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *

def index(request):
    meal = Product.objects.filter(status='meal')
    drink = Product.objects.filter(status='drink')
    context = {
        'meal': meal,
        'drink': drink,
    }
    return render(request,'index.html',context)
def menu(request):
    meal = Product.objects.filter(status='meal')
    drink = Product.objects.filter(status='drink')
    desert = Product.objects.filter(status='dessert')
    context = {
        'meal': meal,
        'drink': drink,
        'desert': desert,

    }
    return render(request,'menu.html',context)
def team(request):
    team = Team.objects.all()
    return render(request,'team.html',{'team':team})
def about_product(request,id):
    product = Product.objects.get(id=id)
    return render(request,'about_product.html',{'product':product})
def about(request):
    return render(request,'about.html',{})
def login(request):
    return render(request,'login and signup.html',{})