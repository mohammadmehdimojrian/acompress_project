from django.shortcuts import render


def index_render(request):
    return render(request , 'index.html')
# Create your views here.
