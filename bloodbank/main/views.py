from django.shortcuts import render, redirect
from .models import Donor
def home(request):
    return render(request, 'home.html')
def add_donor(request):
    if request.method == 'POST':