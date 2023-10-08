from django import forms
from crud.models import ClassRoom, Student


class ClassRoomForm(forms.Form):
    name = forms.CharField(max_length=20)


class ClassRoomModelForm(forms.ModelForm):
    # is_active = forms.BooleanField()  # in case of extra field
    class Meta:
        model = ClassRoom
        fields = ["name", ]



# class StudentForm(forms.ModelFor):
#     contact = forms.CharField()
#     address = forms.CharField()
#
#     class Meta:
#         model = Student
#         fields = ["name", "email", "age", "classroom", "contact", "address"]
