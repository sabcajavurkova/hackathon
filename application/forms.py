from django import forms
from django.core.validators import MinLengthValidator
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
    
    