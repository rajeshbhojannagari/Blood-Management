from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_donor, name='add_donor'),
    path('donors/', views.donors, name='donors'),
]