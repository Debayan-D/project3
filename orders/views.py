from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Sum
from .models import Category,Regular_pizza,Sicilian_pizza,Topping,Sub,Pasta,Salad,Dinner_platter,Order,User_order,Order_counter

# Create your views here.
counter = Order_counter.objects.first()
if counter == None:
    set_counter = Order_counter(counter=1)
    set_counter.save()
superuser = User.objects.filter(is_superuser=True)
if superuser.count() == 0:
    superuser=User.objects.create_user("admin", "admin@admin.com", "AdminerAdminer")
    superuser.is_superuser=True
    superuser.is_staff=True
    superuser.save()
    set_superuser=User_order(user=superuser, order_number=counter.counter)
    set_superuser.save()


def index(request):
    return HttpResponse("Project 3: TODO")
