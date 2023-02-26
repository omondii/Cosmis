from django import forms
from .models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
        'current_status': forms.TextInput(attrs={'class': 'form-control'}),
        'adm_number': forms.NumberInput(attrs={'class': 'form-control'}),
        'full_name': forms.TextInput(attrs={'class': 'form-control'}),
        'surname': forms.TextInput(attrs={'class': 'form-control'}),
        'gender': forms.TextInput(attrs={'class': 'form-control'}),
        'date_of_admision': forms.DateInput(attrs={'class': 'form-control'}),
        'address': forms.TextInput(attrs={'class': 'form-control'}),
        'date_of_birth': forms.DateInput(attrs={'class': 'form-control'}),
        }