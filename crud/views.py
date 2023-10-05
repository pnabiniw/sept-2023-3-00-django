from django.shortcuts import render, redirect
from .models import ClassRoom, Student, StudentProfile


def classroom(request):
    if request.method == "POST":
        name = request.POST.get("name")
        ClassRoom.objects.create(name=name)
        return redirect("crud_classroom")
    classrooms = ClassRoom.objects.all()
    return render(request, template_name="crud/classroom.html",
                  context={"title": "Classroom", "classrooms": classrooms})


def classroom_delete(request, id):
    classroom = ClassRoom.objects.get(id=id)
    if request.method == "POST":
        classroom.delete()
        return redirect("crud_classroom")
    return render(request, template_name="crud/classroom_delete.html",
                  context={"title": "Classroom Delete", "classroom": classroom})


def classroom_update(request, id):
    if request.method == "POST":
        name = request.POST.get("name")
        ClassRoom.objects.filter(id=id).update(name=name)
        return redirect("crud_classroom")
    classroom = ClassRoom.objects.get(id=id)
    return render(request, template_name="crud/classroom_update.html",
                  context={"title": "Classroom Update", "classroom": classroom})


def student(request):
    students = Student.objects.all()
    return render(request, template_name="crud/student.html",
                  context={"title": "Student", "students": students})


def add_student(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        address = request.POST.get("address")
        contact = request.POST.get("contact")
        pp = request.FILES.get('pp')
        std = Student.objects.create(name=name, email=email, age=age, classroom_id=1)
        sp = StudentProfile.objects.create(contact=contact, address=address, student=std)
        if pp:
            sp.profile_picture = pp
            sp.save()
        return redirect("crud_student")
    return render(request, template_name="crud/add_student.html",
                  context={"title": "Add Student"})
