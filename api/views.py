from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from crud.models import Student


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
            })
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
        # for student in students:
        #     response.append({
        #         "name": student.name,
        #         "age": student.age,
        #         "email": student.email,
        #         "classroom": student.classroom.name
        #     })
        return Response(response)
