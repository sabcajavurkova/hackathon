from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mac_address = models.CharField(validators=[MinLengthValidator(17)], max_length=17)
    is_present = models.BooleanField(default=False)
    is_in_school = models.BooleanField(default=False)
    
    objects = models.Manager()
    class LectureManager(models.Manager):
        def create_lecture(self, name, students, teacher):
            return self.create(name=name, students=students, teacher=teacher)
    
    lectures = LectureManager()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mac_address = models.CharField(validators=[MinLengthValidator(17)], max_length=17)
    
    objects = models.Manager()
    class LectureManager(models.Manager):
        def create_lecture(self, name, students, teacher):
            return self.create(name=name, students=students, teacher=teacher)
        
    lectures = LectureManager()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
   
    
class Lecture(models.Model):
    name = models.CharField(max_length=20)
    students = models.ManyToManyField(Student, related_name='students')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher')
    
    def __str__(self):
        return f"{self.name} taught by {self.teacher.last_name}"
