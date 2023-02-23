from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from django.urls import reverse
from core.models import Subject,AcademicTerm, AcademicYear

Gender = (
    ("Male", "Male"), 
    ("Female", "Female"),
    )
Status = (
    ("Active", "Active"), 
    ("Inactive","Inactive"),
    )

# Create your models here.
class Student(models.Model):
    current_status = models.TextField(choices=Status, max_length=10)
    adm_number = models.PositiveIntegerField(primary_key=True)
    full_name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, choices=Gender)
    date_of_admission = models.DateField(auto_now_add=True)
    address = models.TextField(max_length=120)
    date_of_birth = models.DateField(default=timezone.now)
    #passport = models.ImageField(blank=True, upload_to="students/passports/")
    class Meta:
        ordering = ["full_name"]
    def __str__(self):
        return f'{self.adm_number} {self.full_name} {self.surname}'
    def get_absolute_url(self):
        return reverse("student-detail", kwargs={"pk": self.pk})  

class Teacher(models.Model):
    current_status = models.TextField(choices=Status, max_length=10)
    tsc_number = models.PositiveIntegerField(primary_key=True)
    full_name = models.TextField(max_length=200)
    surname = models.TextField(max_length=200)
    gender = models.TextField(choices=Gender, max_length=10)
    date_joined = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=15)
    mobile_num_regex = RegexValidator(regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!")
    phone_number = models.CharField(validators=[mobile_num_regex], max_length=13, blank=True)
    def __str__(self):
        return f'{self.tsc_number} {self.full_name} {self.surname}'

    def get_absolute_url(self):
        return reverse("teacher-detail", kwargs={"pk": self.pk})

class Parents(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    mobile_num_regex = RegexValidator(regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!")
    phone_number = models.CharField(validators=[mobile_num_regex], max_length=13, blank=True)
    email = models.EmailField(max_length=200)
    def __str__(self):
        return f'Parents: {self.name} {self.phone_number}'
    def get_absolute_url(self):
        return reverse("parent-detail", kwargs={"pk": self.pk})

class ClassTeachers(models.Model):
    id = models.AutoField(primary_key=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)


