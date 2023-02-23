from django import forms
from django.forms import ModelForm, modelformset_factory

from .models import AcademicTerm, AcademicYear, Subject, StudentClass


class AcademicYearForm(ModelForm):
    prefix = "Academic Year"

    class Meta:
        model = AcademicYear
        fields = ["name", "current"]


class AcademicTermForm(ModelForm):
    prefix = "Academic Term"

    class Meta:
        model = AcademicTerm
        fields = ["name", "current"]


class SubjectForm(ModelForm):
    prefix = "Subject"

    class Meta:
        model = Subject
        fields = ["name"]


class StudentClassForm(ModelForm):
    prefix = "Class"

    class Meta:
        model = StudentClass
        fields = ["name"]


class CurrentYearForm(forms.Form):
    current_year = forms.ModelChoiceField(
        queryset=AcademicYear.objects.all(),
        help_text='Click <a href="/year/create/?next=current-year/">here</a> to add new year',
    )
    current_term = forms.ModelChoiceField(
        queryset=AcademicTerm.objects.all(),
        help_text='Click <a href="/term/create/?next=current-year/">here</a> to add new term',
    )
