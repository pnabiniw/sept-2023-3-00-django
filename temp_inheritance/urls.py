from django.urls import path
from .views import student, model_student


urlpatterns = [
    path('student/', model_student),
    path("", student)
]
