from django.urls import path
from .views import hello_world, MessageView, SimpleStudentView, \
    SimpleStudentListView, ClassRoomDetailAPIView, ClassRoomAPIView, StudentAPIView, \
    StudentDetailAPIView


urlpatterns = [
    path("hello-world/", hello_world),
    path("message/", MessageView.as_view()),
    path("simple-student-list/", SimpleStudentListView.as_view()),
    path("simple-student/<int:id>/", SimpleStudentView.as_view()),
]

urls_with_serializers = [
    path("classroom/<int:id>/", ClassRoomDetailAPIView.as_view()),
    path("student/<int:id>/", StudentDetailAPIView.as_view()),
    path("classroom/", ClassRoomAPIView.as_view()),
    path("student/", StudentAPIView.as_view()),
]

urlpatterns += urls_with_serializers
