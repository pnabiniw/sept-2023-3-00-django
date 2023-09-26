from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return self.name


class StudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    contact = models.CharField(max_length=14)
    address = models.CharField(max_length=20)
    roll_no = models.IntegerField()
