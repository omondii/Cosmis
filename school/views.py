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

def addstud(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = StudentForm()
    return render(request, 'tables/add.html', {'form':form})