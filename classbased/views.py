from django.shortcuts import render, redirect
from crud.models import ClassRoom, Student, StudentProfile
from .forms import ClassRoomForm, ClassRoomModelForm


def classroom(request):
    if request.method == "POST":
        # name = request.POST.get("name")  # raw data without validation
        form = ClassRoomForm(request.POST)  # Validation Runs here
        if form.is_valid():  # checks whether submitted form valid or not
            name = form.cleaned_data.get("name")
            ClassRoom.objects.create(name=name)
        return redirect("cb_classroom")
    form = ClassRoomForm()
    classrooms = ClassRoom.objects.all()
    return render(request, template_name='classbased/classroom.html',
                  context={"title": "Classroom", "classrooms": classrooms,
                           "form": form})


def model_classroom(request):
    if request.method == "POST":
        # name = request.POST.get("name")  # raw data without validation
        form = ClassRoomModelForm(request.POST)  # Validation Runs here
        if form.is_valid():  # checks whether submitted form valid or not
            form.save()
        return redirect("cb_classroom")
    form = ClassRoomModelForm()
    classrooms = ClassRoom.objects.all()
    return render(request, template_name='classbased/classroom.html',
                  context={"title": "Classroom", "classrooms": classrooms,
                           "form": form})
