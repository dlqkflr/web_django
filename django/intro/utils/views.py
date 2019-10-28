from django.shortcuts import render
# import request
# Create your views here.
def index(request):
    return render(request, 'utils/index.html')