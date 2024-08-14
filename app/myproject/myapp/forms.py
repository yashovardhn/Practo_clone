# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Doctor, Patient, Appointment

class DoctorRegistrationForm(UserCreationForm):
    specialization = forms.CharField(max_length=100)
    experience = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'specialization', 'experience']

class PatientRegistrationForm(UserCreationForm):
    age = forms.IntegerField()
    medical_history = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'age', 'medical_history']

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['prescription_file']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'time']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['rating']
        widgets = {
            'rating': forms.TextInput(attrs={'class': 'input'}),
        }

class AppointmentStatusForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['status'] 