from django.db import models

class Users(models.Model):
	name = models.CharField(max_length=100)
	paycheck = models.IntegerField(default=0)
	date_joined = models.DateField()

class Rooms(models.Model):
	department = models.CharField(max_length=100)
	spots = models.IntegerField(default=0)