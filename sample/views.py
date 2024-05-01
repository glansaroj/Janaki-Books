from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def greet(request):
    context = {
        'country': 'Nepal'
    }
    return render(request, 'sample/index.html', context)
