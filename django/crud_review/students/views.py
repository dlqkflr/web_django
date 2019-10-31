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

    if request.method == 'POST':
        student = Students.objects.get(pk=pk)
        student.delete()
    
        return redirect('students:index')

def new(request):
    if request.method == 'POST':
        # students를 생성함.
        name = request.POST.get('name')
        age = request.POST.get('age')

        students = Students.objects.create(name= name , age = age)
        students.save()

        return redirect('/students/')

    else:        
        # new page를 보여주면 됨.
        return render(request, 'students/new.html')

    

# def create(request):
#     name = request.POST.get('name')
#     age = request.POST.get('age')

#     students = Students.objects.create(name= name , age = age)
#     students.save()

#     return redirect('/students/')

def edit(request, pk):
    students = Students.objects.get(pk=pk)
    
    if request.method == 'POST':
        # update (def update)
        name = request.POST.get('name')
        age = request.POST.get('age')
        
    
        students.name = name
        students.age = age
        students.save()

        return redirect('/students/')

    else:
        # 수정하는 페이지 보여줌 
        context ={
            'students':students,
        }
        return render(request, 'students/edit.html', context)




    

# def update(request,pk):

#     name = request.POST.get('name')
#     age = request.POST.get('age')
#     students = Students.objects.get(pk=pk)
    
#     students.name = name
#     students.age = age
#     students.save()

#     return redirect('/students/')
