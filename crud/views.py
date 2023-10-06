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
        class_id = request.POST.get("class_id")
        std = Student.objects.create(name=name, email=email, age=age, classroom_id=class_id)
        sp = StudentProfile.objects.create(contact=contact, address=address, student=std)
        if pp:
            sp.profile_picture = pp
            sp.save()
        return redirect("crud_student")
    return render(request, template_name="crud/add_student.html",
                  context={"title": "Add Student", "classes": ClassRoom.objects.all()})


def student_detail(request, id):
    std = Student.objects.get(id=id)
    return render(request, template_name="crud/student_detail.html",
                  context={"title": "Student Detail", "student": std})


def student_update(request, id):
    std = Student.objects.get(id=id)
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        address = request.POST.get("address")
        contact = request.POST.get("contact")
        pp = request.FILES.get('pp')
        Student.objects.filter(id=id).update(name=name, email=email, age=age)
        sp, _ = StudentProfile.objects.update_or_create(student=std, defaults={"address": address,
                                                                               "contact": contact})  # (object, True)
        if pp:
            sp.profile_picture = pp
            sp.save()
        return redirect("student_detail", std.id)

    return render(request, template_name="crud/student_update.html",
                  context={"title": "Student Update", "student": std})


