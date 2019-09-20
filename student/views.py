from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from student.models import Student

@login_required
def stud_render(request):
    student = Student.objects.get(jmbag = request.user.username)

    context = {'student': student}

    return render(request, 'student.html', context)
        