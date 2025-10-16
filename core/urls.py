from django.urls import path
from . import views
urlpatterns = [
  path('', views.dashboard, name='dashboard'),
  path('login/', views.user_login, name='login'),
  path('logout/', views.user_logout, name='logout'),
  path('register/', views.user_register, name='register'),
  path('students/', views.students, name='students'),
  path('students/add/', views.student_add, name='student_add'),
  path('student/<int:pk>/', views.student_detail, name='student_detail'),
]
