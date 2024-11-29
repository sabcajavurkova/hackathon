from django import forms
from django.core.validators import MinLengthValidator
from django.forms import ModelForm
from .models import Student, Teacher, Lecture

class RegisterUserForm(forms.Form):
    GROUP_CHOICES = (
        ('Ucitel', 'Ucitel'),
        ('Zak', 'Zak')
    )
    role = forms.ChoiceField(
        choices=GROUP_CHOICES,
        widget=forms.Select,
        required=True,
        label='Role uživatele',
    )

    mac_address = forms.CharField(validators=[MinLengthValidator(17)], max_length=17, required=True, label='MAC adresa')
    username = forms.CharField(max_length=20, required=True, label='Username')
    first_name = forms.CharField(max_length=20, required=True, label='Křestní jméno')
    last_name = forms.CharField(max_length=20, required=True, label='Příjmení')
    password = forms.CharField(widget=forms.PasswordInput)
    
    
class AddLectureForm(forms.Form):
    """students = Student.objects.all()
    stud_CHOICES = []
    for student in students:
        stud_CHOICES.append((student, student))

    stud_CHOICES = tuple(stud_CHOICES)

    name = forms.CharField(max_length=20)
    #students = forms.MultipleChoiceField(choices=stud_CHOICES)
    students = forms.ModelMultipleChoiceField(
        queryset=Student.objects.all(),
        widget=forms.SelectMultiple,
        required=True,
    )
    teachers = Teacher.objects.all()
    CHOICES = []
    for teacher in teachers:
        CHOICES.append((teacher.id, teacher))


    CHOICES = tuple(CHOICES)
    teacher = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.Select,
        required=True,
    )"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['students'].widget.attrs['students'] = 'form-control'
        self.fields['teacher'].widget.attrs['teacher'] = 'form-control'
    