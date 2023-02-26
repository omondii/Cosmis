from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Student, Teacher
from .forms import StudentForm
# Create your views here.
@login_required
def studentTableView(request):
    all_students = Student.objects.all()
    return render(request, 'tables/studenttables.html', {'all_students':all_students})

def teachersTableView(request):
    all_teachers = Teacher.objects.all()
    return render(request, 'tables/teacherstable.html',{'all_teachers':all_teachers})

def addStud(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_current_status = form.cleaned_data.get('current_status')
            new_adm_number = form.cleaned_data.get('adm_number')
            new_full_name = form.cleaned_data.get('full_name')
            new_surname = form.cleaned_data.get('surname')
            new_gender = form.cleaned_data.get('gender')
            new_date_of_admission = form.cleaned_data.get('date_of _admission')
            new_address = form.cleaned_data.get('address')
            new_date_of_birth = form.cleaned_data.get('date_of_birth')

            new_student = Student(
                current_status = new_current_status,
                adm_number = new_adm_number,
                full_name = new_full_name,
                surname = new_surname,
                gender = new_gender,
                date_of_admission = new_date_of_admission,
                address = new_address,
                date_of_birth = new_date_of_birth,
            )
            new_student.save()
            return render(request, 'tables\add.html',{
                'form':StudentForm(),
                'success':True
            })
    else:
        form =StudentForm()
    return render(request, 'tables\add.html',{
            'form': StudentForm()
            })