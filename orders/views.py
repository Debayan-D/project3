from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Sum
from .models import Category,Regular_pizza,Sicilian_pizza,Topping,Sub,Pasta,Salad,Dinner_platter,Order,User_order,Order_counter

# Create your views here.

def index(request):
    return HttpResponse("Project 3: TODO")
