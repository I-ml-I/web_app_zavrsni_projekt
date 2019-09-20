from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

@login_required
def redirect_render(request):
    user = request.user

    if user is not None:
        if user.groups.filter (name='student'):
            return HttpResponseRedirect('/student/')
        elif user.groups.filter (name='profesor'):
            return HttpResponseRedirect('/profesor/')
        elif user.groups.filter (name='administrator'):
            return HttpResponseRedirect('/administrator/')

    context = {}
    template = "index.html"
    return render(request, template, context)