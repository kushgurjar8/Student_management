from django.contrib import admin
from .models import Student, Semester, Subject


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_no', 'semester_id', 'contact')
    list_filter = ('semester_id',)
    search_fields = ('name', 'roll_no')


@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('name', 'course_id')
    list_filter = ('course_id',)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'course_id', 'semester_id')
    search_fields = ('name', 'code')