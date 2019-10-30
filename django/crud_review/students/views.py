from django.shortcuts import render, redirect
from .models import Students

# Create your views here.
def index(request):
    students = Students.objects.all().order_by('-id')
    context ={
        'students': students,
    }
    return render(request, 'students/index.html', context)

def detail(request, pk):
    students = Students.objects.get(pk=pk)

    context = {
        'students':students,
    }
    return render(request, 'students/detail.html', context)

def delete(request,pk):
    student = Students.objects.get(pk=pk)
    student.delete()
    
    return redirect('/students/')

def new(request):
    return render(request, 'students/new.html')

def create(request):
    name = request.POST.get('name')
    age = request.POST.get('age')

    students = Students.objects.create(name= name , age = age)
    
    return redirect('/students/')

def edit(request, pk):
    students = Students.objects.get(pk=pk)
    context ={
        'students':students,
    }
    return render(request, 'students/edit.html', context)

def update(request,pk):

    name = request.POST.get('name')
    age = request.POST.get('age')
    students = Students.objects.get(pk=pk)
    
    students.name = name
    students.age = age
    students.save()

    return redirect('/students/')
