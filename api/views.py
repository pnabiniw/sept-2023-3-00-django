from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, \
    DestroyAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from crud.models import Student, ClassRoom, StudentProfile

from .serializers import ClassRoomSerializer, ClassRoomModelSerializer, StudentModelSerializer, \
    StudentProfileModelSerializer


def hello_world(request):
    response = {"message": "Hello World"}
    return JsonResponse(response)


class MessageView(APIView):
    def get(self, *args, **kwargs):
        return Response([
            {"name": "Jon", "address": "KTM", "age": 30},
            {"name": "Alex", "address": "KTM", "age": 30},
            {"name": "Bruce", "address": "KTM", "age": 30},
        ])


class SimpleStudentView(APIView):
    def get(self, *args, **kwargs):
        try:
            student = Student.objects.get(id=kwargs.get("id"))
        except Student.DoesNotExist:
            return Response({
                "detail": "Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
        return Response({
            "name": student.name,
            "email": student.email,
            "age": student.age,
            "classroom": student.classroom.name
        })

# Comprehension, ternary if, decorators, tuple packing unpacking, json handling (loads and dumps),
# lambda, map, reduce, filter
class SimpleStudentListView(APIView):
    def get(self, *args, **kwargs):
        students = Student.objects.all()
        response = [{"name": student.name, "age": 30, "email": student.email} for student in students]
        return Response(response)

    def post(self, *args, **kwargs):
        print(self.request.data)
        name = self.request.data.get("name")
        email = self.request.data.get("email")
        age = self.request.data.get("age")
        classroom = self.request.data.get("classroom")
        Student.objects.create(name=name, email=email, age=age, classroom_id=classroom)
        return Response({
            "detail": "Student created successfully !!"
        }, status=status.HTTP_201_CREATED)


class ClassRoomDetailAPIView(APIView):
    def get(self, *args, **kwargs):
        try:
            classroom = ClassRoom.objects.get(id=kwargs['id'])
        except ClassRoom.DoesNotExist:
            return Response({
                "detail": "Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = ClassRoomSerializer(classroom)  # Serialization
        return Response(serializer.data)


class ClassRoomAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ClassRoomModelSerializer(data=request.data)
        if serializer.is_valid():
            # name = serializer.validated_data.get("name")
            # ClassRoom.objects.create(name=name)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, *args, **kwargs):
        classrooms = ClassRoom.objects.all()
        serializer = ClassRoomModelSerializer(classrooms, many=True)
        return Response(serializer.data)


class StudentDetailAPIView(APIView):
    def get(self, *args, **kwargs):
        try:
            student = Student.objects.get(id=kwargs['id'])
        except Student.DoesNotExist:
            return Response({
                "detail": "Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
        ser = StudentModelSerializer(student)
        return Response(ser.data)


class StudentAPIView(APIView):
    def get(self, *args, **kwargs):
        students = Student.objects.all()
        ser = StudentModelSerializer(students, many=True, context={"request": self.request})
        return Response(ser.data)

    def post(self, *args, **kwargs):
        ser = StudentModelSerializer(data=self.request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)


class StudentProfileAPIView(APIView):
    def get(self, request, *args, **kwargs):
        profiles = StudentProfile.objects.all()
        ser = StudentProfileModelSerializer(profiles, many=True, context={"request": self.request})
        return Response(ser.data)

    def post(self, *args, **kwargs):
        ser = StudentProfileModelSerializer(data=self.request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)


class ClassRoomListAPIView(ListAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer


class ClassRoomCreateAPIView(CreateAPIView):
    # queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer


class ClassRoomRetrieveAPIView(RetrieveAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer


class ClassRoomUpdateAPIView(UpdateAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer


class ClassRoomDeleteAPIView(DestroyAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer


class ClassRoomListCreateAPIView(ListCreateAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer


class ClassRoomObjectAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer
            

# class ListAPIView:
#     queryset = None
#     serializer = None
#
#     def get(self, *args, **kwargs):
#         queryset = self.queryset
#         ser = self.serializer(queryset, many=True)
#         return Response(ser.data)
