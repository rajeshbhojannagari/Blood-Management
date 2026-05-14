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
        phone = request.POST['phone']

        Donor.objects.create(
            name=name,
            age=age,
            blood_group=blood_group,
            city=city,
            phone=phone
        )
        return redirect('donors')
    return render(request, 'add_donor.html')