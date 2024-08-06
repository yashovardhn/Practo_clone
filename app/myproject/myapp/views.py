from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import DoctorRegistrationForm, PatientRegistrationForm, PrescriptionForm
from .models import User, Doctor, Patient, Appointment, Schedule
from django.contrib.auth.decorators import login_required

# myapp/views.py


def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'myapp/doctor_list.html', {'doctors': doctors})


def doctor_detail(request, user_id):
    doctor = get_object_or_404(Doctor, user__id=user_id)
    return render(request, 'myapp/doctor_detail.html', {'doctor': doctor})


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
    return render(request, 'myapp/register_doctor.html', {'form': form})

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
    return render(request, 'myapp/register_patient.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.user_type == 'patient':
                login(request, user)
                return redirect('patient_dashboard')
            elif user.user_type == 'doctor':
                login(request, user)
                return redirect('doctor_dashboard')
            else:
                return render(request, 'myapp/login.html', {'error': 'Invalid user type'})
        else:
            return render(request, 'myapp/login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'myapp/login.html')

@login_required(login_url='login')
def doctor_dashboard(request):
    appointments = Appointment.objects.filter(doctor__user=request.user)
    schedule = Schedule.objects.filter(doctor__user=request.user)
    return render(request, 'myapp/doctor_dashboard.html', {'appointments': appointments, 'schedule': schedule})

@login_required(login_url='login')
def patient_dashboard(request):
    appointments = Appointment.objects.filter(patient__user=request.user)
    return render(request, 'myapp/patient_dashboard.html', {'appointments': appointments})

@login_required(login_url='login')
def add_prescription(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == 'POST':
        form = PrescriptionForm(request.POST, request.FILES, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('doctor_dashboard')
    else:
        form = PrescriptionForm(instance=appointment)
    return render(request, 'myapp/add_prescription.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')
