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
def donors(request):
    donor_list = Donor.objects.all()
    return render(request, 'donors.html', {'donors': donor_list})
def search(request):
    query = request.GET.get('blood_group')
    result = Donor.objects.filter(blood_group=query)
    return render(request, 'search.html', {'result': result})