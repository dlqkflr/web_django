from django.shortcuts import render, redirect
from .models import Movies


# Create your views here.
def index(request):
    movies = Movies.objects.all().order_by('id')
    context ={
        'movies': movies,
    }

    return render(request, 'movies/index.html', context)

def new(request):
    return render(request, 'movies/new.html')

def create(request):
    title = request.POST.get('title')
    title_en = request.POST.get('title_en')
    audience = request.POST.get('audience')
    open_date = request.POST.get('open_date')
    genre = request.POST.get('genre')
    watch_grade = request.POST.get('watch_grade')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')

    movies = Movies.objects.create(title = title, title_en = title_en, audience= audience,
                                    open_date = open_date, genre= genre, watch_grade = watch_grade,
                                    score= score, poster_url = poster_url, description = description)
    movies.save()

    return redirect('/movies/')

def detail(request, pk):
    movies = Movies.objects.get(pk=pk)
    context = {
        'movies' : movies,
    }

    return render(request, 'movies/detail.html', context)



def edit(request, pk):

    movies = Movies.objects.get(pk=pk)

    context = {
        'movies':movies,
    }

    return render(request, 'movies/edit.html', context)


def update(request, pk):

    title = request.POST.get('title')
    title_en = request.POST.get('title_en')
    audience = request.POST.get('audience')
    open_date = request.POST.get('open_date')
    genre = request.POST.get('genre')
    watch_grade = request.POST.get('watch_grade')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')


    movies = Movies.objects.get(pk=pk)
    movies.title = title
    movies.title_en = title_en
    movies.audience= audience
    movies.open_date = open_date
    movies.genre= genre 
    movies.watch_grade = watch_grade
    movies.score= score
    movies.poster_url = poster_url
    movies.description = description

    movies.save()

    return redirect('/movies/')

def delete(request, pk):

    movies = Movies.objects.get(pk=pk)
    movies.delete()    


    return redirect('/movies/')

