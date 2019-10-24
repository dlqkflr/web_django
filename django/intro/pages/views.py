from django.shortcuts import render
import random

# Create your views here.

def index(request):
    
    context = {
        'name': 'bkpark'
    }
    return render(request, 'index.html', context)

#Template Variable
def dinner(request):

    foods= ['초밥', '카레','칼국수']
    pick = random.choice(foods)
    context = {
        'pick' : pick,
    }

    

    return render(request, 'dinner.html', context)

#Variable Routing
def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'hello.html', context)


#실습
# 1. '이름'과 '나이'를 Variable Routing을 통해 받아서 자기소개
def introduce(request, name, age):
    context = {
        'name' : name,
        'age' : age,
    }
    return render(request, 'introduce.html', context)
# 2. 숫자 2개를 Variable Routing을 통해 받아 곱셈 결과 보여주기

def multiple(request, num1, num2):
    context = {
        'num1': num1,
        'num2': num2,
        'multinum' : num1*num2,
    }
    return render(request, 'multiple.html', context)

from datetime import datetime


def dtl(request):

    foods= ['짜장면','냉면','라면','짬뽕']
    my_sentence = 'Life is short, you need python'
    messages = ['apple','banana', 'mango']
    datetimenow = datetime.now()
    empty_list = []

    context = {
        'foods' : foods,
        'my_sentence' : my_sentence,
        'messages' : messages,
        'datetimenow' : datetimenow,
        'empty_list' : empty_list,
    }

    return render(request, 'dtl.html', context)
    



#[실습]
#is it your birthday?
#오늘이 자기 자신의 생일이면 '예'를 , 아니면 '아니오'를 보여주는 페이지

def birth(request):
    result = ( datetime.now().month == 12 and datetime.now().day == 25 )

    context = {
        'result': result,
    }
    return render(request, 'birth.html', context)