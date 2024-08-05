# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/doctor/', views.register_doctor, name='register_doctor'),
    path('register/patient/', views.register_patient, name='register_patient'),
    path('doctor/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('patient/dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('appointment/<int:appointment_id>/prescription/', views.add_prescription, name='add_prescription'),
]
