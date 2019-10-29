from django.shortcuts import render
from .models import Article
# Create your views here.

def index(request):
    articles = Article.objects.all() #=> QuerySet like list

    context = {
        'articles' : articles,
    }

    return render(request, 'articles/index.html', context)

def new(request):
  
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article.objects.create(title=title, content = content)


    context = {
        'title' : title,
        'content' : content,
    }
    return render(request, 'articles/create.html', context)


