from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from administrator.models import Student, Upisanipredmet, Predmet, Mjesto, Profesor
import re


@login_required
def admin_render(request):
    studenti = Student.objects.all
    profesori = Profesor.objects.all

    context = {'profesori': profesori, 'studenti': studenti}

    template = "administrator.html"
    
    return render(request, template, context)


def dodavanje_osobe(request):
    uloga = request.POST['uloga']
    ime = request.POST['ime']
    prezime = request.POST['prezime']
    jmbag = request.POST['jmbag']
    spol = request.POST['spol']
    email = request.POST['email']
    postanskibrojrod = request.POST['pbrRod']
    postanskibrojprb = request.POST['pbrPbr']
    datumrod = request.POST['datumRodjenja']

    if(uloga == 'student'):
        noviStudent = Student(jmbag, prezime, ime, spol, datumrod, postanskibrojprb, postanskibrojrod, email)
        noviStudent.save()
    elif(uloga == 'profesor'):
        noviProfesor = Profesor(jmbag, prezime, ime, spol, datumrod, postanskibrojprb, postanskibrojrod, email)
        noviProfesor.save()
    

    return HttpResponseRedirect('/administrator')

def brisanje_profesora(request, profjmbag):
    profZaObrisati = Profesor.objects.get(jmbag = profjmbag)
    profZaObrisati.delete()
    return HttpResponseRedirect('/administrator')


def brisanje_studenta(request, studjmbag):
    print("----------" + str(studjmbag))
    studZaObrisati = Student.objects.get(jmbag = studjmbag)
    studZaObrisati.delete()
    return HttpResponseRedirect('/administrator')



