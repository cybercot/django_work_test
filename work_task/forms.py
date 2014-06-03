#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from django import forms
from django.forms.extras.widgets import SelectDateWidget

from work_task.models import Users
class UsersForm(forms.ModelForm):
    name = forms.CharField(max_length=100, help_text="Имя"),
    paycheck = forms.IntegerField(help_text="Зарплата"),
    date_joined = forms.DateField(widget = SelectDateWidget(), help_text="Дата поступления на работу"),
    class Meta:
        model = Users
from work_task.models import Rooms
class RoomsForm(forms.ModelForm):
    department = forms.CharField(max_length=100, help_text="Отдел"),
    spots = forms.IntegerField(help_text="Вместимость"),
    date = forms.DateField(widget = SelectDateWidget(), help_text="Дата"),
    class Meta:
        model = Rooms
