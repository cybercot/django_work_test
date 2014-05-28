from django.template import RequestContext
from django.shortcuts import render_to_response
from work_task.models import Users,Rooms

def index(request):
	context = RequestContext(request)
	users = Users.objects.order_by('name')
	rooms = Rooms.objects.order_by('spots')
	context_dict = {'users':users,'rooms':rooms}
	return render_to_response('work_task/table.html', context_dict, context)
