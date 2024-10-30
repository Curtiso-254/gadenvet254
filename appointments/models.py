# appointments/models.py
from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.DurationField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('canceled', 'Canceled')
    ]

    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.TimeField()
    veterinarian = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    client_name = models.CharField(max_length=255)  # Added field
    client_email = models.EmailField(default='default@example.com')  # Added default value
    message = models.TextField(blank=True, null=True)  # Added field

    def __str__(self):
        return f'{self.service.name} on {self.date} at {self.time_slot} with {self.veterinarian}'
