from django.urls import path
from .views import student, model_student, student_profile


urlpatterns = [
    path('student/', model_student, name='student'),
    path('student-profile/', student_profile, name='student_profile'),
    path("", student, name="inherit")
]
