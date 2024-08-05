# myapp/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from .forms import DoctorRegistrationForm, PatientRegistrationForm, PrescriptionForm
from .models import User, Doctor, Patient, Appointment, Schedule

def register_doctor(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = 'doctor'
            user.save()
            Doctor.objects.create(user=user, specialization=form.cleaned_data['specialization'], experience=form.cleaned_data['experience'])
            login(request, user)
            return redirect('doctor_dashboard')
    else:
        form = DoctorRegistrationForm()
    return render(request, 'register_doctor.html', {'form': form})

def register_patient(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = 'patient'
            user.save()
            Patient.objects.create(user=user, age=form.cleaned_data['age'], medical_history=form.cleaned_data['medical_history'])
            login(request, user)
            return redirect('patient_dashboard')
    else:
        form = PatientRegistrationForm()
    return render(request, 'register_patient.html', {'form': form})

def doctor_dashboard(request):
    appointments = Appointment.objects.filter(doctor__user=request.user)
    schedule = Schedule.objects.filter(doctor__user=request.user)
    return render(request, 'doctor_dashboard.html', {'appointments': appointments, 'schedule': schedule})

def patient_dashboard(request):
    appointments = Appointment.objects.filter(patient__user=request.user)
    return render(request, 'patient_dashboard.html', {'appointments': appointments})

def add_prescription(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == 'POST':
        form = PrescriptionForm(request.POST, request.FILES, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('doctor_dashboard')
    else:
        form = PrescriptionForm(instance=appointment)
    return render(request, 'add_prescription.html', {'form': form})


# Create your views here.
