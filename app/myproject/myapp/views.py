from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import DoctorRegistrationForm, PatientRegistrationForm, PrescriptionForm, AppointmentForm, RatingForm
from .models import User, Doctor, Patient, Appointment, Schedule
from django.urls import reverse_lazy
from django.core.files.storage import default_storage
from django.http import HttpResponse, FileResponse, Http404
import os

class DoctorListView(ListView):
    model = Doctor
    template_name = 'myapp/doctor_list.html'
    context_object_name = 'doctors'

class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'myapp/doctor_detail.html'
    pk_url_kwarg = 'user_id'

    def get_object(self):
        return get_object_or_404(Doctor, user__id=self.kwargs['user_id'])

class RegisterDoctorView(CreateView):
    form_class = DoctorRegistrationForm
    template_name = 'myapp/register_doctor.html'
    success_url = reverse_lazy('doctor_dashboard')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.user_type = 'doctor'
        user.save()
        Doctor.objects.create(user=user, specialization=form.cleaned_data['specialization'], experience=form.cleaned_data['experience'])
        login(self.request, user)
        return super().form_valid(form)

class RegisterPatientView(CreateView):
    form_class = PatientRegistrationForm
    template_name = 'myapp/register_patient.html'
    success_url = reverse_lazy('patient_dashboard')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.user_type = 'patient'
        user.save()
        Patient.objects.create(user=user, age=form.cleaned_data['age'], medical_history=form.cleaned_data['medical_history'])
        login(self.request, user)
        return super().form_valid(form)

class LoginView(View):
    def get(self, request):
        return render(request, 'myapp/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.user_type == 'patient':
                return redirect('patient_dashboard')
            elif user.user_type == 'doctor':
                return redirect('doctor_dashboard')
        else:
            return render(request, 'myapp/login.html', {'error': 'Invalid credentials'})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class DoctorDashboardView(LoginRequiredMixin, ListView):
    template_name = 'myapp/doctor_dashboard.html'
    context_object_name = 'appointments'
    login_url = 'login'

    def get_queryset(self):
        return Appointment.objects.filter(doctor__user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['schedule'] = Schedule.objects.filter(doctor__user=self.request.user)
        return context

class AppointmentDetailView(DetailView):
    model = Appointment
    template_name = 'appointment_detail.html'  # Ensure this template exists
    context_object_name = 'appointment'


class PatientDashboardView(LoginRequiredMixin, ListView):
    template_name = 'myapp/patient_dashboard.html'
    context_object_name = 'appointments'
    login_url = 'login'

    def get_queryset(self):
        return Appointment.objects.filter(patient__user=self.request.user)

class AddPrescriptionView(LoginRequiredMixin, UpdateView):
    model = Appointment
    form_class = PrescriptionForm
    template_name = 'myapp/add_prescription.html'
    pk_url_kwarg = 'appointment_id'
    success_url = reverse_lazy('doctor_dashboard')
    login_url = 'login'

class BookAppointmentView(LoginRequiredMixin, CreateView):
    form_class = AppointmentForm
    template_name = 'myapp/book_appointment.html'
    login_url = 'login'

    def form_valid(self, form):
        doctor = get_object_or_404(Doctor, user__id=self.kwargs['doctor_id'])
        appointment = form.save(commit=False)
        appointment.doctor = doctor
        appointment.patient = get_object_or_404(Patient, user=self.request.user)
        appointment.status = 'pending'
        appointment.save()
        return redirect('patient_dashboard')

class DownloadPrescriptionView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, id):
        try:
            appointment = Appointment.objects.get(id=id)
            if appointment.prescription_file:
                file_path = default_storage.path(appointment.prescription_file.name)
                if os.path.exists(file_path):
                    response = FileResponse(open(file_path, 'rb'), content_type='application/pdf')
                    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
                    response['Content-Length'] = os.path.getsize(file_path)
                    return response
                else:
                    raise Http404("Prescription file not found")
            else:
                raise Http404("No prescription file available")
        except Appointment.DoesNotExist:
            raise Http404("Appointment does not exist")

class RateAppointmentView(LoginRequiredMixin, UpdateView):
    model = Appointment
    form_class = RatingForm
    template_name = 'myapp/rate_appointment.html'
    success_url = reverse_lazy('patient_dashboard')
    login_url = 'login'
