# myapp/admin.py
from django.contrib import admin
from .models import User, Doctor, Patient, Appointment, Schedule

admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Schedule)
