from django.db import models

class Users(models.Model):
	name = models.CharField(max_length=100)
	paycheck = models.IntegerField(default=0)
	date_joined = models.DateField()