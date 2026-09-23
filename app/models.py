from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name


class Semester(models.Model):
    name = models.CharField(max_length=20)
    course_id = models.IntegerField()


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    course_id = models.IntegerField()
    semester_id = models.IntegerField()


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20)
    course_id = models.IntegerField()
    semester_id = models.IntegerField()
    date_of_birth = models.DateField()
    contact = models.CharField(max_length=15)
    address = models.TextField()
    photo = models.ImageField(upload_to='student_photos/')
