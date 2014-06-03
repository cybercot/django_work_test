#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from work_task.models import *
from work_task.forms import *
import yaml
from django.db.models.loading import get_model

def table(request):
	# View for index page
	context = RequestContext(request)
	schema = yaml.load(open('test.yaml'))
	classes = []
	for class_name in schema:
		classes.append(class_name.capitalize())
	return render_to_response('work_task/base.html', {'classes':classes}, context)

def upload_table(request):
	# View for upload table functionality
	context = RequestContext(request)
	cat_name = None
	response_data = None
	# List for column names
	help_text = ['id']
	# List for values
	class_attr = {}
	# Id of date field
	date_id=''
	if request.method == 'GET':
		# Get model name
		cat_name = request.GET['category_id']
	if cat_name:
		# Get model
		my_model = get_model('work_task',cat_name)
		# Get objects
		models = my_model.objects.order_by('id')
		for model in models:
			class_attr[model]=[]
			for f in model._meta.fields:
				class_attr[model].append({getattr(model,f.name):f.name})
		for i in range(1,len(model._meta.fields)):
			help_text.append(model._meta.fields[i].help_text)
		n = 0
		for f in model._meta.fields:
			n+=1
			if str(type(getattr(model,f.name))) == "<type 'datetime.date'>":
				date_id = n
	return render_to_response('work_task/upload_table.html', {'help_text':help_text,'class_attr':class_attr, 
		'cat_name':cat_name, 'date_id':date_id,}, context)
		

def update_data(request):
	# View for update data in tables
	context = RequestContext(request)
	cat_name = None
	if request.method == "GET":
		cat_id,cat_name,newContent,class_id,class_name = request.GET['data'].split('-')
	if cat_name:
		my_model = get_model('work_task',cat_name)
		row = my_model.objects.get(id=int(cat_id))
		if class_name == 'datepicker':
			m,d,y = newContent.split('/')
			newContent = y+'-'+m+'-'+d
			setattr(row,class_id,newContent)
		else:
			setattr(row,class_id,newContent)
		row.save()
	return HttpResponse("Hello")

def add_users(request):
	context = RequestContext(request)
	form = UsersForm()
	return render_to_response('work_task/add_users.html', {'form':form}, context)