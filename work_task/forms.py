#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from django import forms
from work_task.models import *
from django.forms.extras.widgets import SelectDateWidget

class UsersForm(forms.ModelForm):
    name = forms.CharField(max_length=100, help_text="Имя")
    paycheck = forms.IntegerField(help_text="Зарплата")
    date_joined = forms.DateField(widget=SelectDateWidget(), help_text="Дата поступления на работу")
    model_name = forms.CharField(widget=forms.TextInput(attrs={"readonly":"readonly"}), initial = "Users")
    class Meta:
        model = Users
class RoomsForm(forms.ModelForm):
    department = forms.CharField(max_length=100, help_text="Отдел")
    spots = forms.IntegerField(help_text="Вместимость")
    date = forms.DateField(widget=SelectDateWidget(), help_text="Дата")
    model_name = forms.CharField(widget=forms.TextInput(attrs={"readonly":"readonly"}), initial = "Rooms")
    class Meta:
        model = Rooms
