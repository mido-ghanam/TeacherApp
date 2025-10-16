from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Teacher, Student, Attendance, Grade
from .forms import StudentForm, AttendanceForm, GradeForm
def user_register(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = User.objects.create_user(username=username, password=password)
    Teacher.objects.create(user=user)
    return redirect('login')
  return render(request, 'register.html')
def user_login(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user:
      login(request, user)
      return redirect('dashboard')
  return render(request, 'login.html')
def user_logout(request):
  logout(request)
  return redirect('login')
@login_required
def dashboard(request):
  teacher = get_object_or_404(Teacher, user=request.user)
  students = Student.objects.filter(teacher=teacher)
  today = Attendance.objects.filter(student__in=students).order_by('-date')[:10]
  return render(request, 'dashboard.html', {'students': students,'attendance': today})
@login_required
def students(request):
  teacher = get_object_or_404(Teacher, user=request.user)
  students = Student.objects.filter(teacher=teacher)
  return render(request, 'students.html', {'students': students})
@login_required
def student_add(request):
  teacher = get_object_or_404(Teacher, user=request.user)
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      s = form.save(commit=False)
      s.teacher = teacher
      s.save()
      return redirect('students')
  else:
    form = StudentForm()
  return render(request, 'student_form.html', {'form': form})
@login_required
def student_detail(request, pk):
  student = get_object_or_404(Student, pk=pk)
  attendances = Attendance.objects.filter(student=student).order_by('-date')
  grades = Grade.objects.filter(student=student).order_by('-date')
  return render(request, 'student_detail.html', {'student': student,'attendances': attendances,'grades': grades})
