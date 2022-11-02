from django.shortcuts import render, redirect, reverse
from .models import Student
from django.contrib import messages

# Create your views here.

def student_list(request):
    stud_list = Student.objects.all().order_by('name')
    return render(request, 'index.html', {"stud_list": stud_list})

def student_update(request, stud_id):
    student = Student.objects.get(pk=stud_id)
    context = {
        'student': student,
        'update': True
    }
    return render(request, 'create.html', context)

def student_add(request):        
    return render(request, 'create.html', {"update": False } )

def student_delete(reqeust, stud_id):
    student = Student.objects.get(pk=stud_id)
    student.delete()
    return redirect(reverse('home'))