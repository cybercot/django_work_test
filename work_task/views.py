#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from work_task.models import Users,Rooms
from django.http import HttpResponse
from work_task.forms import UsersForm

def table(request):
	# View for index page
	context = RequestContext(request)
	return render_to_response('work_task/base.html', {}, context)

def upload_table(request):
	# View for upload table functionality
	context = RequestContext(request)
	cat_name = None
	response_data = None

	if request.method == 'GET':
		cat_name = request.GET['category_id']
	if cat_name:
		if cat_name == 'Users':
			users = Users.objects.order_by('id')
			return render_to_response('work_task/upload_table.html', {'users':users}, context)
		

def update_data(request):
	context = RequestContext(request)
	cat_name = None
	if request.method == "GET":
		cat_id,cat_name,newContent,class_id = request.GET['data'].split('-')
	if cat_name:
		if cat_name == "Users":
			row = Users.objects.get(id=int(cat_id))
			if class_id == 'name':
				row.name = newContent
			elif class_id == 'paycheck':
				row.paycheck = newContent
			elif class_id == 'datepicker':
				m,d,y = newContent.split('/')
				newContent = y+'-'+m+'-'+d
				row.date_joined = newContent
			else:
				row.id = newContent
		else:
			row = Rooms.objects.get(id=int(cat_id))
			if class_id == "department":
				row.department = newContent
			elif class_id == "spots":
				row.spots = newContent
			else:
				row.id = newContent
		row.save()
	return HttpResponse("Hello")

def add_users(request):
	context = RequestContext(request)
	form = UsersForm()
	return render_to_response('work_task/add_users.html', {'form':form}, context)