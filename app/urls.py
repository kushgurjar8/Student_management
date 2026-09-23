from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.course_list, name='courses'),
    path('courses/add/', views.course_create, name='course_create'),
    path('create-course/', views.create_course, name='create_course'),
    path('courses/edit/', views.course_update, name='course_update'),
    path('update-course/', views.update_course, name='update_course'),
    path('courses/delete/', views.course_delete, name='course_delete'),
    path('delete-course/', views.delete_course, name='delete_course'),
    path('students/', views.student_list, name='student_list'),
    path('students/<int:id>/', views.student_detail, name='student_detail'),
    path('create/', views.create, name='create'),
    path('create-student/', views.create_student, name='create_student'),
    path('update/', views.update, name='update'),
    path('update-student/', views.update_student, name='update_student'),
    path('delete/', views.delete, name='delete'),
    path('delete-student/', views.delete_student, name='delete_student'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
