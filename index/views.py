from django.shortcuts import render
from django.http import HttpResponseRedirect

def index_render(request):
    if (request.user.is_authenticated):
        return HttpResponseRedirect('/redirect/')

    else:
        return render(request, 'index.html')
