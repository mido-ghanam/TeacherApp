from django.db import models
from django.contrib.auth.models import User
class Teacher(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  phone = models.CharField(max_length=30, blank=True)
  def __str__(self):
    return self.user.get_full_name() or self.user.username
class Student(models.Model):
  teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
  name = models.CharField(max_length=120)
  roll = models.CharField(max_length=50, blank=True)
  grade = models.CharField(max_length=30, blank=True)
  def __str__(self):
    return self.name
class Attendance(models.Model):
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  date = models.DateField()
  present = models.BooleanField(default=True)
  def __str__(self):
    return f"{self.student.name} - {self.date}"
class Grade(models.Model):
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  subject = models.CharField(max_length=100)
  value = models.FloatField()
  date = models.DateField(auto_now_add=True)
  def __str__(self):
    return f"{self.student.name} - {self.subject}: {self.value}"
