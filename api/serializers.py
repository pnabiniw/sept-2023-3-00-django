from rest_framework import serializers
from crud.models import ClassRoom, Student


class ClassRoomSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)


class ClassRoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ["id", "name"]


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
