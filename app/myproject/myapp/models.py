# myapp/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()
    # Add other metadata fields

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    medical_history = models.TextField()
    doctors = models.ManyToManyField(Doctor, through='Appointment')
    # Add other metadata fields

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=10, choices=(('pending', 'Pending'), ('confirmed', 'Confirmed'), ('completed', 'Completed')))
    rating = models.IntegerField(null=True, blank=True)
    visit_details = models.TextField(null=True, blank=True)
    prescription_file = models.FileField(upload_to='prescriptions/', null=True, blank=True)  # Add this field

class Schedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    day = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()
    slot_duration = models.IntegerField()  # Duration in minutes


# Create your models here.
