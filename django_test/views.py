from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect


def index(request):
	context = RequestContext(request)
	return HttpResponseRedirect('/table/')