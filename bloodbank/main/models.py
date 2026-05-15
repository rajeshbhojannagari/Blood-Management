from django.db import models
class Donor(models.Model):
    BLOOD_GROUPS = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ]
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name