from django.urls import path
from .views import classroom, model_classroom, ClassRoomView, ClassRoomTemplateView, \
    ClassRoomCreateView, StudentListView


urlpatterns = [
    path("classroom/", classroom, name="cb_classroom"),
    path("simple-classroom/", ClassRoomView.as_view()),
    path("template-classroom/", ClassRoomTemplateView.as_view()),
    path("create-classroom/", ClassRoomCreateView.as_view()),
    path("student-list/", StudentListView.as_view()),
    path("model-classroom/", model_classroom, name="cb_model_classroom"),
]
