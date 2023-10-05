from django.urls import path
from .views import classroom, classroom_delete, classroom_update, \
    student, add_student

urlpatterns = [
    path("student/", student, name="crud_student"),
    path("add-student/", add_student, name="add_student"),
    path("class/delete/<int:id>/", classroom_delete, name="classroom_delete"),
    path("class/update/<int:id>/", classroom_update, name="classroom_update"),
    path("", classroom, name="crud_classroom")
]
