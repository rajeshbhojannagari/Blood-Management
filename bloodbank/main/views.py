from django.shortcuts import render, redirect
from .models import Donor
def home(request):
    return render(request, 'home.html')
def add_donor(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        blood_group = request.POST['blood_group']
        city = request.POST['city']