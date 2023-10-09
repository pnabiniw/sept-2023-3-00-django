from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from crud.models import ClassRoom, Student, StudentProfile
from .forms import ClassRoomForm, ClassRoomModelForm
from django.views import View
from django.views.generic import TemplateView, CreateView, ListView


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


class ClassRoomView(View):
    def get(self, *args, **kwargs):
        classrooms = ClassRoom.objects.all()
        form = ClassRoomModelForm()
        return render(self.request, template_name="classbased/classroom.html",
                      context={"classrooms": classrooms, "form": form})

    def post(self, *args, **kwargs):
        form = ClassRoomModelForm(self.request.POST)
        if form.is_valid():
            form.save()
        return redirect('cb_classroom')


class ClassRoomTemplateView(TemplateView):
    template_name = "classbased/classroom.html"

    def get_context_data(self, **kwargs):
        context = {"classrooms": ClassRoom.objects.all(), "form": ClassRoomModelForm()}
        return context


class ClassRoomCreateView(CreateView):
    form_class = ClassRoomModelForm
    queryset = ClassRoom.objects.all()
    template_name = "classbased/classroom.html"
    success_url = reverse_lazy("cb_classroom")

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["classrooms"] = self.queryset
        print(context)
        return context


class StudentListView(ListView):
    queryset = Student.objects.all()
    template_name = "classbased/student.html"
    context_object_name = "students"

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context["students"] = self.queryset
    #     return context  # student_list
