from django.shortcuts import render
from django.http import HttpResponse

def index(request):
 #   return HttpResponse('hello from posts')
    return render(request, 'posts/index.html', {
        'title':'moshe is the best'
    })