from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .forms import RegisterUserForm, AddLectureForm
from .models import Student, Teacher, Lecture
from datetime import datetime, timedelta

def index(request):
    return render(request, 'index.html')

def index_teacher(request):
    user = request.user
    if hasattr(user, 'student_profile') and user:
        student = user.student_profile
        lectures = Lecture.objects.filter(students=student)
        return render(request, 'index-student.html', {'lectures': lectures})
    
    context = {}
    if hasattr(user, 'teacher_profile'):
        teacher = user.teacher_profile
        lectures = Lecture.objects.filter(teacher=teacher)
        context ={'lectures': lectures}
        
    
    return render(request, 'index-teacher.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get("username").lower()
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user:
            auth_login(request, user)
            return redirect('/')
        
        messages.success(request, 'Pri prihlasovani nastala chyba')
        return redirect('/prihlaseni')
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data['role']
            username = form.cleaned_data['username'].lower()
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            mac_address = form.cleaned_data['mac_address']
            password = form.cleaned_data['password']
            
            user = User.objects.create_user(username=username, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            
            if role == 'Zak':
                Student.objects.create(user=user, first_name=first_name, last_name=last_name, mac_address=mac_address)
            elif role == 'Ucitel':
                Teacher.objects.create(user=user, first_name=first_name, last_name=last_name, mac_address=mac_address)
            
            auth_login(request, user)
            return redirect('/')
    else:
        form = RegisterUserForm()
    return render(request, 'signup.html', {'form': form})



last_status_change = {}


class BluetoothDataView(APIView):
    def post(self, request, *args, **kwargs):
        mac_address = request.data.get('address')
        device = request.data.get('device')

        if not mac_address:
            return Response({"error": "MAC address is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            student = Student.objects.get(mac_address=mac_address)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

        # Logika pro master_node (škola)
        if device == 'master_node':
            if student.is_in_school:
                student.is_in_school = False
                student.is_present = False  # Reset is_present pokud opustil školu
            else:
                student.is_in_school = True  # Student přichází do školy
            student.save()

            return Response({
                "message": f"Student {student.first_name} {student.last_name} has {'entered' if student.is_in_school else 'left'} the school.",
                "is_in_school": student.is_in_school,
                "is_present": student.is_present
            }, status=status.HTTP_200_OK)

        # Logika pro slave_node (třída)
        elif device == 'slave_node':
            if not student.is_present:
                student.is_present = True  # Student vstoupil do třídy, takže změna na True
            else:
                student.is_present = False  # Student opustil třídu, změna na False
            student.save()

            return Response({
                "message": f"Student {student.first_name} {student.last_name} has {'entered' if student.is_present else 'left'} the classroom.",
                "is_in_school": student.is_in_school,
                "is_present": student.is_present
            }, status=status.HTTP_200_OK)

        return Response({"error": "Invalid device type."}, status=status.HTTP_400_BAD_REQUEST)


        
    
        
def list_lecture(request, pk):
    lecture = Lecture.objects.get(pk=pk)
    students = lecture.students.all()
    return render(request, 'list_lecture.html', {'lecture': lecture, 'students': students})

def logout_user(request):
    logout(request)
    return redirect('/')

def add_lecture(request):
    if request.method == 'POST':
        form = AddLectureForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            students = form.cleaned_data['students']
            teacher_id = form.cleaned_data['teacher']
            
            teacher = Teacher.objects.get(id=teacher_id)
            
            lecture = Lecture.objects.create(name=name, teacher=teacher)
            lecture.students.set(students)
            return redirect('/')
    else:
        form = AddLectureForm()
    return render(request, 'add_lecture.html', {'form': form})

def remove_lecture(request, pk):
    lecture = Lecture.objects.get(pk=pk)
    lecture.delete()
    return redirect('/')
