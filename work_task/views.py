#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from work_task.models import Users,Rooms
from django.http import HttpResponse

def table(request):
	context = RequestContext(request)
	return render_to_response('work_task/base.html', {}, context)

def upload_table(request):
	context = RequestContext(request)
	cat_name = None
	response_data = None

	if request.method == 'GET':
		cat_name = request.GET['category_id']
	if cat_name:
		if cat_name == 'Users':
			response_data='<h2 class="sub-header">Users</h2>'
			users = Users.objects.order_by('name')
			if users:
				response_data = response_data+'<table class="table table-striped"><thead><tr><th>id</th><th>Имя</th><th>Зарплата</th><th>Дата поступления на работу</th></tr></thead><tbody>'
				for user in users:
					response_data=response_data+'<tr><td class="id">'+str(user.id)+'</td><td class="name">'+str(user.name)+'</td><td class="paycheck">'+str(user.paycheck)+'</td><td class="datepicker">'+str(user.date_joined)+'</td></tr>'
				response_data=response_data+'</tbody></table>'
			else:
				response_data='<strong>There are no users present.</strong>'
		else:
			rooms = Rooms.objects.order_by('spots')
			response_data = '<h2 class="sub-header">Rooms</h2>'
			if rooms:
				response_data=response_data+'<table class="table table-striped"><thead><tr><th>id</th><th>Отдел</th><th>Вместимость</th></tr></thead><tbody>'
				for room in rooms:
					response_data=response_data+'<tr><td class="id">'+str(room.id)+'</td><td>'+str(room.department)+'</td><td>'+str(room.spots)+'</td></tr>'
				response_data=response_data+'</tbody></table>'
			else:
				response_data='<strong>There are no rooms present.</strong>'
	return HttpResponse(response_data)

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
			elif class_id == 'date_joined':
				row.date_joined = newContent
			else:
				row.id = newContent
			row.save()
	return HttpResponse("Hello")