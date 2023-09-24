from django.shortcuts import render


def student(request):
    students = [
        {"name": "Jon", "age": 30, "address": "KTM"},
        {"name": "Jane", "age": 20, "address": "PKR"},
        {"name": "Alex", "age": 23, "address": "BKT"},
        {"name": "Hary", "age": 40, "address": "LTP"},
    ]
    return render(request, template_name="temp_inheritance/student.html", context={"students": students})
