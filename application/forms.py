from django import forms
from django.core.validators import MinLengthValidator
from .models import Student, Teacher, Lecture

class RegisterUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=20, required=True, label='Křestní jméno')
    last_name = forms.CharField(max_length=20, required=True, label='Příjmení')
    mac_address = forms.CharField(validators=[MinLengthValidator(17)], max_length=17, required=True, label='Příjmení')
    