from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Student
# Create your views here.
@login_required
def studentTableView(request):
    all_students = Student.objects.all()
    return render(request, 'tables/studenttables.html', {'all_students':all_students})