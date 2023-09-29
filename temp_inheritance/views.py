from django.shortcuts import render
from .models import Student, StudentProfile


def student(request):
    students = [
        {"name": "Jon", "age": 30, "address": "KTM"},
        {"name": "Jane", "age": 20, "address": "PKR"},
        {"name": "Alex", "age": 23, "address": "BKT"},
        {"name": "Hary", "age": 40, "address": "LTP"},
    ]
    return render(request, template_name="temp_inheritance/student.html", context={"students": students})


def model_student(request):
    students = Student.objects.all()  # queryset => [obj1, obj2, obj3]
    return render(request, template_name="temp_inheritance/model_student.html",
                  context={"students": students})


def student_profile(request):
    profiles = StudentProfile.objects.all()
    return render(request, 'temp_inheritance/profile.html', {"profiles": profiles})
