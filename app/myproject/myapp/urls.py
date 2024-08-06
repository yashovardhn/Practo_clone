# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/doctor/', views.register_doctor, name='register_doctor'),
    path('register/patient/', views.register_patient, name='register_patient'),
    path('doctor/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('patient/dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('appointment/<int:appointment_id>/prescription/', views.add_prescription, name='add_prescription'),
    path('appointment/book/<int:doctor_id>/', views.book_appointment, name='book_appointment'),  # New URL for booking appointment
    path('logout/', views.logout_user, name='logout'),
    path('login/', views.login_user, name='login'),
    path('', views.doctor_list, name='doctor_list'),
    path('doctor/<int:user_id>/', views.doctor_detail, name='doctor_detail'),
    path('prescription/<int:id>/', views.download_prescription, name='download_prescription'),
    path('appointment/<int:pk>/rate/', views.rate_appointment, name='rate_appointment'),
]