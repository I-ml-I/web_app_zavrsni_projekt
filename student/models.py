from django.db import models

class Mjesto(models.Model):
    postanskibroj = models.CharField(primary_key=True, max_length=5)
    naziv = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'mjesto'

class Student(models.Model):
    jmbag = models.CharField(primary_key=True, max_length=10)
    prezime = models.CharField(max_length=25)
    ime = models.CharField(max_length=25)
    spol = models.CharField(max_length=1)
    datumrod = models.DateField()
    postanskibrojprb = models.ForeignKey(Mjesto, models.DO_NOTHING, db_column='postanskibrojprb', blank=True, null=True, related_name='studPbr')
    postanskibrojrod = models.ForeignKey(Mjesto, models.DO_NOTHING, db_column='postanskibrojrod', blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'
