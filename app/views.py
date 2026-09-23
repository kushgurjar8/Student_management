from django.shortcuts import render, redirect
from django.contrib import auth, messages
from .models import *




def home(request):
    students = Student.objects.all()
    semesters = Semester.objects.all()
    courses = Course.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'home.html', {
        'students': students,
        'semesters': semesters,
        'courses': courses,
        'subjects': subjects,
    })


def course_list(request):
    if not request.user.is_authenticated:
        return redirect('login')

    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})


def course_create(request):
    return render(request, 'course_create.html')


def create_course(request):
    if request.method == 'POST':
        name = request.POST['name']
        code = request.POST['code']
        description = request.POST['description']

        Course.objects.create(name=name, code=code, description=description)

    return redirect('courses')


def course_update(request):
    return render(request, 'course_update.html')


def update_course(request):
    if request.method == 'POST':
        id = request.POST['id']
        name = request.POST['name']
        code = request.POST['code']
        description = request.POST['description']

        Course.objects.filter(id=id).update(name=name, code=code, description=description)

    return render(request, 'course_updated.html')


def course_delete(request):
    return render(request, 'course_delete.html')


def delete_course(request):
    if request.method == 'POST':
        id = request.POST['id']
        Course.objects.filter(id=id).delete()

    return redirect('course_delete')


def student_list(request):
    students = Student.objects.all()

    semester_id = request.GET.get('semester')
    if semester_id:
        students = students.filter(semester_id=semester_id)

    context = {
        'students': students,
        'semesters': Semester.objects.all(),
        'selected_semester': semester_id or '',
    }
    return render(request, 'student_list.html', context)


def student_detail(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'student_detail.html', {'student': student})


def create(request):
    return render(request, 'create.html', {
        'courses': Course.objects.all(),
    })


def create_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        roll_no = request.POST['roll_no']
        course_id = request.POST['course_id']
        semester_id = request.POST['semester_id']
        date_of_birth = request.POST['date_of_birth']
        contact = request.POST['contact']
        address = request.POST['address']
        photo = request.FILES['photo']

        Student.objects.create(
            name=name, roll_no=roll_no, course_id=course_id, semester_id=semester_id,
            date_of_birth=date_of_birth, contact=contact, address=address,
            photo=photo,
        )

    return redirect('student_list')


def update(request):
    return render(request, 'update.html', {
        'courses': Course.objects.all(),
    })


def update_student(request):
    if request.method == 'POST':
        id = request.POST['id']
        name = request.POST['name']
        roll_no = request.POST['roll_no']
        course_id = request.POST['course_id']
        semester_id = request.POST['semester_id']
        date_of_birth = request.POST['date_of_birth']
        contact = request.POST['contact']
        address = request.POST['address']
        photo = request.FILES['photo']

        student = Student.objects.get(id=id)
        student.name = name
        student.roll_no = roll_no
        student.course_id = course_id
        student.semester_id = semester_id
        student.date_of_birth = date_of_birth
        student.contact = contact
        student.address = address
        student.photo = photo
        student.save()

    return render(request, 'update_students.html')


def delete(request):
    return render(request, 'delete.html')


def delete_student(request):
    if request.method == 'POST':
        id = request.POST['id']
        Student.objects.filter(id=id).delete()

    return redirect('delete')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

