from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from profesor.models import Profesor

@login_required
def prof_render(request):
    profesor = Profesor.objects.get(jmbag = request.user.username)

    context = {'profesor': profesor}

    template = "profesor.html"
    
    return render(request, template, context)
