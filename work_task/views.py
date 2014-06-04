#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from work_task.models import *
from work_task.forms import *
import yaml
from django.db.models.loading import get_model
import re
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
import time
from django.shortcuts import render
from django.http import HttpResponseBadRequest
from django.conf import settings

def table(request):
	# View for index page
	context = RequestContext(request)
	schema = yaml.load(open('test.yaml'))
	classes = []
	for class_name in schema:
		classes.append(class_name.capitalize())
	return render_to_response('work_task/base.html', {'classes':classes}, context)

@method_decorator(csrf_exempt)
def upload_table(request):
	# View for upload table functionality
	context = RequestContext(request)
	cat_name = None
	# List for column names
	help_text = ['id']
	# List for values
	class_attr = {}
	# Id of date field
	date_id=''
	if request.method == 'POST':
		# Get model name
		cat_name = request.POST['category_id']
	if cat_name:
		# Get model
		my_model = get_model('work_task',cat_name)
		# Get objects
		models = my_model.objects.order_by('id')
		if models:
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
		else:
			return render_to_response('work_task/upload_table.html', {'help_text':help_text,'class_attr':class_attr, 
		'cat_name':cat_name, 'date_id':date_id,}, context)
		

def update_data(request):
	# View for update data in tables
	error_message=''
	context = RequestContext(request)
	cat_name = None
	if request.method == "GET":
		cat_id,cat_name,newContent,class_id,class_name = request.GET['data'].split('-')
	if cat_name:
		my_model = get_model('work_task',cat_name)
		row = my_model.objects.get(id=int(cat_id))
		if class_name == 'datepicker':
			test, error_message = test_data(newContent,"<type 'datetime.date'>")
			if test:
				m,d,y = newContent.split('/')
				newContent = y+'-'+m+'-'+d
				setattr(row,class_id,newContent)
				row.save()
		else:
			test, error_message = test_data(newContent,str(type(getattr(row,class_id))))
			if test:
				setattr(row,class_id,newContent)
				row.save()
	return HttpResponse(error_message)

def upload_form(request):	
    if request.POST:
        if settings.DEBUG:
            time.sleep(2)  # Only for load demo
        class_name = request.POST.get('model_name')
        class_name+='Form'
        form = eval(class_name)(request.POST)
        if form.is_valid():
        	form.save(commit=True)
        	# Only executed with jQuery form request
        	if request.is_ajax():
        		return HttpResponse('OK')
        	else:
        		pass
        else:
        	if request.is_ajax():
        		# Prepare JSON for parsing
        		errors_dict = {}
        		if form.errors:
        			for error in form.errors:
        				e = form.errors[error]
        				errors_dict[error] = unicode(e)
        		return HttpResponseBadRequest(json.dumps(errors_dict))
        	else:
        		pass
    else:
        cat_name = request.GET['category_id']
        cat_name+='Form'
        form = eval(cat_name)()
    return render(request, 'work_task/upload_form.html', {'form':form})

def test_data(data,type):
	if type == "<type 'datetime.date'>":
		a = re.compile("^[0-9]{2}\/[0-9]{2}\/[0-9]{4}$")
		if a .match(data):
			return (True, 'Correct!!!')
		else:
			return (False, 'Error!!!')
		return (True, 'Correct!!!')
	elif type == "<type 'int'>":
		a = re.compile("^([0-9]+)$")
		if a.match(data):
			return (True, 'Correct!!!')
		else:
			return (False, 'Error!!!')
	elif type == "<type 'unicode'>":
		a = re.compile("^[A-z0-9]+$")
		if a.match(data):
			return (True, 'Correct!!!')
		else:
			return (False, 'Error!!!')
	else:
		return (False, 'Error!!!')