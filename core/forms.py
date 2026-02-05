from django import forms
from .models import Student, Attendance, Grade
class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ['name','roll','grade']
class AttendanceForm(forms.ModelForm):
  class Meta:
    model = Attendance
    fields = ['date','present']
class GradeForm(forms.ModelForm):
  class Meta:
    model = Grade
    fields = ['subject','value']
