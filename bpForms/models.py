from django.db import models

class Project(models.Model):
    bloodtype = [('A+','A+'), ('B+','B+'), ('AB+','AB+'), ('O-','O-'),]
    firstName=models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    bloodType=models.CharField(max_length=20, choices=bloodtype,default='O-')
    pinCode = models.CharField(max_length=10)
