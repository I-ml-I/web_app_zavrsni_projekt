from django.db import models

class Mjesto(models.Model):
    postanskibroj = models.CharField(primary_key=True, max_length=5)
    naziv = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'mjesto'


class Predmet(models.Model):
    id = models.IntegerField(primary_key=True)
    naziv = models.CharField(max_length=70)
    jmbagnositelja = models.ForeignKey('Profesor', models.CASCADE, db_column='jmbagnositelja')

    class Meta:
        managed = False
        db_table = 'predmet'


class Profesor(models.Model):
    jmbag = models.CharField(primary_key=True, max_length=10)
    prezime = models.CharField(max_length=25)
    ime = models.CharField(max_length=25)
    spol = models.CharField(max_length=1)
    datumrod = models.DateField(blank=True, null=True)
    postanskibrojprb = models.ForeignKey(Mjesto, models.CASCADE, db_column='postanskibrojprb', blank=True, null=True, related_name='profpbr')
    postanskibrojrod = models.ForeignKey(Mjesto, models.CASCADE, db_column='postanskibrojrod', blank=True, null=True)
    sluzbenimail = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'profesor'


class Student(models.Model):
    jmbag = models.CharField(primary_key=True, max_length=10)
    prezime = models.CharField(max_length=25)
    ime = models.CharField(max_length=25)
    spol = models.CharField(max_length=1)
    datumrod = models.DateField()
    postanskibrojprb = models.ForeignKey(Mjesto, models.CASCADE, db_column='postanskibrojprb', blank=True, null=True, related_name='studPbr')
    postanskibrojrod = models.ForeignKey(Mjesto, models.CASCADE, db_column='postanskibrojrod', blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


class Upisanipredmet(models.Model):
    idpredmeta = models.ForeignKey(Predmet, models.CASCADE, db_column='idpredmeta', primary_key=True)
    jmbagstudenta = models.ForeignKey(Student, models.CASCADE, db_column='jmbagstudenta')
    ocjena = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'upisanipredmet'
        unique_together = (('idpredmeta', 'jmbagstudenta'),)
