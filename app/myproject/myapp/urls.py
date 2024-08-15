from django.urls import path
from .views import DoctorDashboardView, PatientDashboardView, DoctorListView, DoctorDetailView, BookAppointmentView, RegisterDoctorView, RegisterPatientView, DownloadPrescriptionView, RateAppointmentView, LoginView, LogoutView,UpdateAppointmentStatusView, UploadPrescriptionView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/doctor/', RegisterDoctorView.as_view(), name='register_doctor'),
    path('register/patient/', RegisterPatientView.as_view(), name='register_patient'),
    path('doctor-dashboard/', DoctorDashboardView.as_view(), name='doctor_dashboard'),
    path('patient/dashboard/', PatientDashboardView.as_view(), name='patient_dashboard'),
    path('appointment/book/<int:doctor_id>/', BookAppointmentView.as_view(), name='book_appointment'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('', DoctorListView.as_view(), name='doctor_list'),
    path('doctor/<int:user_id>/', DoctorDetailView.as_view(), name='doctor_detail'),
    path('appointment/<int:pk>/rate/', RateAppointmentView.as_view(), name='rate_appointment'),
    path('update_status/<int:pk>/', UpdateAppointmentStatusView.as_view(), name='update_status'),
    path('upload-prescription/<int:appointment_id>/', UploadPrescriptionView.as_view(), name='upload_prescription'),
     path('download-prescription/<int:id>/', DownloadPrescriptionView.as_view(), name='download_prescription'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

