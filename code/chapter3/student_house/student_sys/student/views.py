from django.shortcuts import render

# Create your views here.
from student.models import Student


def index(request):
    students = Student.object.all()
    return render(request, 'index.html', context={'students': students})