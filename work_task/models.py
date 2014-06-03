#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from django.db import models
Users = type("Users",(models.Model,), {"name":models.CharField(max_length=100, help_text="Имя"),"paycheck":models.IntegerField(default=0, help_text="Зарплата"),"date_joined":models.DateField(help_text="Дата поступления на работу"),"__module__":"work_task.models"})
Rooms = type("Rooms",(models.Model,), {"department":models.CharField(max_length=100, help_text="Отдел"),"spots":models.IntegerField(default=0, help_text="Вместимость"),"date":models.DateField(help_text="Дата"),"__module__":"work_task.models"})
