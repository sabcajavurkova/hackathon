from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

from .forms import RegisterUserForm
from .models import Student, Teacher, Lecture

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
            username = form.cleaned_data['username']
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

class BluetoothDataView(APIView):
    def post(self, request, *args, **kwargs):
        # Получаем MAC-адрес из запроса
        mac_address = request.data.get('address')

        if not mac_address:
            return Response({"error": "MAC address is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Ищем студента с таким MAC-адресом
            student = Student.objects.get(mac_address=mac_address)
            serializer = StudentSerializer(student, data=request.data, partial=True)

            if serializer.is_valid():
                # Обновляем информацию
                serializer.save()
                return Response({"message": f"Student {student.first_name} {student.last_name} is now in school."}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Student.DoesNotExist:
            return Response({"message": "MAC address not found in the database."}, status=status.HTTP_404_NOT_FOUND)
        
def list_lecture(request, pk):
    lecture = Lecture.objects.get(pk=pk)
    students = lecture.students.all()
    return render(request, 'list_lecture.html', {'lecture': lecture, 'students': students})

def logout_user(request):
    logout(request)
    return redirect('/')