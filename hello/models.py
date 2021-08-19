from django.db import models

# Create your models here.
from django.db import models
from django.contrib import admin

# Create your models here.from django.db import models
#
# # Create your models here.
class Guntur(models.Model):
     SNO = models.CharField(default='',max_length=100)
     Hospital = models.CharField(default=0, max_length=200)
     HelpDeskNumber  =  models.CharField(max_length=30, default='')
     NodalOfficerNumber = models.CharField(default=0,max_length=200)
     AarogyasriEmpanelmentstatus = models.CharField(default=0,max_length=200)
     ICUAvailable = models.CharField(default=0,max_length=200)
     O2Available = models.CharField(default=0,max_length=200)
     GeneralAvailable = models.CharField(default=0,max_length=200)
     VentilatorAvailable= models.CharField(default=0,max_length=200)

     def __str__(self):
          return self.Hospital

class EG(models.Model):
     SNO = models.CharField(default='', max_length=100)
     Hospital = models.CharField(default=0, max_length=200)
     HelpDeskNumber = models.CharField(max_length=30, default='')
     NodalOfficerNumber = models.CharField(default=0, max_length=200)
     AarogyasriEmpanelmentstatus = models.CharField(default=0, max_length=200)
     ICUAvailable = models.CharField(default=0, max_length=200)
     O2Available = models.CharField(default=0, max_length=200)
     GeneralAvailable = models.CharField(default=0, max_length=200)
     VentilatorAvailable = models.CharField(default=0, max_length=200)

     def __str__(self):
          return self.Hospital


class WG(models.Model):
     SNO = models.CharField(default='', max_length=100)
     Hospital = models.CharField(default=0, max_length=200)
     HelpDeskNumber = models.CharField(max_length=30, default='')
     NodalOfficerNumber = models.CharField(default=0, max_length=200)
     AarogyasriEmpanelmentstatus = models.CharField(default=0, max_length=200)
     ICUAvailable = models.CharField(default=0, max_length=200)
     O2Available = models.CharField(default=0, max_length=200)
     GeneralAvailable = models.CharField(default=0, max_length=200)
     VentilatorAvailable = models.CharField(default=0, max_length=200)

     def __str__(self):
          return self.Hospital


class Krishna(models.Model):
     SNO = models.CharField(default='', max_length=100)
     Hospital = models.CharField(default=0, max_length=200)
     HelpDeskNumber = models.CharField(max_length=30, default='')
     NodalOfficerNumber = models.CharField(default=0, max_length=200)
     AarogyasriEmpanelmentstatus = models.CharField(default=0, max_length=200)
     ICUAvailable = models.CharField(default=0, max_length=200)
     O2Available = models.CharField(default=0, max_length=200)
     GeneralAvailable = models.CharField(default=0, max_length=200)
     VentilatorAvailable = models.CharField(default=0, max_length=200)

     def __str__(self):
          return self.Hospital


class Prakasam(models.Model):
     SNO = models.CharField(default='', max_length=100)
     Hospital = models.CharField(default=0, max_length=200)
     HelpDeskNumber = models.CharField(max_length=30, default='')
     NodalOfficerNumber = models.CharField(default=0, max_length=200)
     AarogyasriEmpanelmentstatus = models.CharField(default=0, max_length=200)
     ICUAvailable = models.CharField(default=0, max_length=200)
     O2Available = models.CharField(default=0, max_length=200)
     GeneralAvailable = models.CharField(default=0, max_length=200)
     VentilatorAvailable = models.CharField(default=0, max_length=200)

     def __str__(self):
          return self.Hospital


class Nellore(models.Model):
     SNO = models.CharField(default='', max_length=100)
     Hospital = models.CharField(default=0, max_length=200)
     HelpDeskNumber = models.CharField(max_length=30, default='')
     NodalOfficerNumber = models.CharField(default=0, max_length=200)
     AarogyasriEmpanelmentstatus = models.CharField(default=0, max_length=200)
     ICUAvailable = models.CharField(default=0, max_length=200)
     O2Available = models.CharField(default=0, max_length=200)
     GeneralAvailable = models.CharField(default=0, max_length=200)
     VentilatorAvailable = models.CharField(default=0, max_length=200)

     def __str__(self):
          return self.Hospital


class Chittoor(models.Model):
     SNO = models.CharField(default='', max_length=100)
     Hospital = models.CharField(default=0, max_length=200)
     HelpDeskNumber = models.CharField(max_length=30, default='')
     NodalOfficerNumber = models.CharField(default=0, max_length=200)
     AarogyasriEmpanelmentstatus = models.CharField(default=0, max_length=200)
     ICUAvailable = models.CharField(default=0, max_length=200)
     O2Available = models.CharField(default=0, max_length=200)
     GeneralAvailable = models.CharField(default=0, max_length=200)
     VentilatorAvailable = models.CharField(default=0, max_length=200)

     def __str__(self):
          return self.Hospital


class Visakha(models.Model):
     SNO = models.CharField(default='', max_length=100)
     Hospital = models.CharField(default=0, max_length=200)
     HelpDeskNumber = models.CharField(max_length=30, default='')
     NodalOfficerNumber = models.CharField(default=0, max_length=200)
     AarogyasriEmpanelmentstatus = models.CharField(default=0, max_length=200)
     ICUAvailable = models.CharField(default=0, max_length=200)
     O2Available = models.CharField(default=0, max_length=200)
     GeneralAvailable = models.CharField(default=0, max_length=200)
     VentilatorAvailable = models.CharField(default=0, max_length=200)

     def __str__(self):
          return self.Hospital


class Vizianagaram(models.Model):
     SNO = models.CharField(default='', max_length=100)
     Hospital = models.CharField(default=0, max_length=200)
     HelpDeskNumber = models.CharField(max_length=30, default='')
     NodalOfficerNumber = models.CharField(default=0, max_length=200)
     AarogyasriEmpanelmentstatus = models.CharField(default=0, max_length=200)
     ICUAvailable = models.CharField(default=0, max_length=200)
     O2Available = models.CharField(default=0, max_length=200)
     GeneralAvailable = models.CharField(default=0, max_length=200)
     VentilatorAvailable = models.CharField(default=0, max_length=200)

     def __str__(self):
          return self.Hospital


class Srikakulam(models.Model):
     SNO = models.CharField(default='', max_length=100)
     Hospital = models.CharField(default=0, max_length=200)
     HelpDeskNumber = models.CharField(max_length=30, default='')
     NodalOfficerNumber = models.CharField(default=0, max_length=200)
     AarogyasriEmpanelmentstatus = models.CharField(default=0, max_length=200)
     ICUAvailable = models.CharField(default=0, max_length=200)
     O2Available = models.CharField(default=0, max_length=200)
     GeneralAvailable = models.CharField(default=0, max_length=200)
     VentilatorAvailable = models.CharField(default=0, max_length=200)

     def __str__(self):
          return self.Hospital


class Kadapa(models.Model):
     SNO = models.CharField(default='', max_length=100)
     Hospital = models.CharField(default=0, max_length=200)
     HelpDeskNumber = models.CharField(max_length=30, default='')
     NodalOfficerNumber = models.CharField(default=0, max_length=200)
     AarogyasriEmpanelmentstatus = models.CharField(default=0, max_length=200)
     ICUAvailable = models.CharField(default=0, max_length=200)
     O2Available = models.CharField(default=0, max_length=200)
     GeneralAvailable = models.CharField(default=0, max_length=200)
     VentilatorAvailable = models.CharField(default=0, max_length=200)

     def __str__(self):
          return self.Hospital


class Kurnool(models.Model):
     SNO = models.CharField(default='', max_length=100)
     Hospital = models.CharField(default=0, max_length=200)
     HelpDeskNumber = models.CharField(max_length=30, default='')
     NodalOfficerNumber = models.CharField(default=0, max_length=200)
     AarogyasriEmpanelmentstatus = models.CharField(default=0, max_length=200)
     ICUAvailable = models.CharField(default=0, max_length=200)
     O2Available = models.CharField(default=0, max_length=200)
     GeneralAvailable = models.CharField(default=0, max_length=200)
     VentilatorAvailable = models.CharField(default=0, max_length=200)

     def __str__(self):
          return self.Hospital


class Ananthapur(models.Model):
     SNO = models.CharField(default='', max_length=100)
     Hospital = models.CharField(default=0, max_length=200)
     HelpDeskNumber = models.CharField(max_length=30, default='')
     NodalOfficerNumber = models.CharField(default=0, max_length=200)
     AarogyasriEmpanelmentstatus = models.CharField(default=0, max_length=200)
     ICUAvailable = models.CharField(default=0, max_length=200)
     O2Available = models.CharField(default=0, max_length=200)
     GeneralAvailable = models.CharField(default=0, max_length=200)
     VentilatorAvailable = models.CharField(default=0, max_length=200)

     def __str__(self):
          return self.Hospital


