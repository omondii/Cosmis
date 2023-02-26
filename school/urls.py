from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.studentTableView, name='studenttables'),
    path('teachers/', views.teachersTableView, name='teacherstable'),
    path('addstud/', views.addStud, name='add'),
]
