from django.urls import path
from .views import hello_world, MessageView, SimpleStudentView, \
    SimpleStudentListView, ClassRoomDetailAPIView, ClassRoomAPIView, StudentAPIView, \
    StudentDetailAPIView, StudentProfileAPIView, ClassRoomListAPIView, ClassRoomCreateAPIView, \
    ClassRoomRetrieveAPIView, ClassRoomUpdateAPIView, ClassRoomDeleteAPIView, \
    ClassRoomListCreateAPIView, ClassRoomObjectAPIView


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
    path("student-profile/", StudentProfileAPIView.as_view()),
]

generic_urls = [
    path("generic-classroom-list/", ClassRoomListAPIView.as_view()),
    path("generic-classroom-create/", ClassRoomCreateAPIView.as_view()),
    path("generic-classroom/", ClassRoomListCreateAPIView.as_view()),
    path("generic-classroom-detail/<int:pk>/", ClassRoomRetrieveAPIView.as_view()),
    path("generic-classroom-update/<int:pk>/", ClassRoomUpdateAPIView.as_view()),
    path("generic-classroom-delete/<int:pk>/", ClassRoomDeleteAPIView.as_view()),
    path("generic-classroom/<int:pk>/", ClassRoomObjectAPIView.as_view()),
]

urlpatterns += urls_with_serializers + generic_urls
