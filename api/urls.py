from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import hello_world, MessageView, SimpleStudentView, \
    SimpleStudentListView, ClassRoomDetailAPIView, ClassRoomAPIView, StudentAPIView, \
    StudentDetailAPIView, StudentProfileAPIView, ClassRoomListAPIView, ClassRoomCreateAPIView, \
    ClassRoomRetrieveAPIView, ClassRoomUpdateAPIView, ClassRoomDeleteAPIView, \
    ClassRoomListCreateAPIView, ClassRoomObjectAPIView, ClassRoomViewSet, ClassRoomListUpdateViewSet,\
    StudentViewSet
from .login import UserLoginView

router = DefaultRouter()
router.register("classroom-viewset", ClassRoomViewSet)
router.register("classroom-list-update", ClassRoomListUpdateViewSet)
router.register("student-viewset", StudentViewSet, basename="student_viewset")


urlpatterns = [
    path("hello-world/", hello_world),
    path("message/", MessageView.as_view()),
    path("simple-student-list/", SimpleStudentListView.as_view()),
    path("simple-student/<int:id>/", SimpleStudentView.as_view()),
    path("login/", UserLoginView.as_view(), name='login')
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

urlpatterns += urls_with_serializers + generic_urls + router.urls
