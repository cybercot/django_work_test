from django.conf.urls import patterns, url
from work_task import views

urlpatterns = patterns('',
	url(r'^$', views.table, name='table'),
	url(r'^upload_table/$', views.upload_table, name='upload_table'),
	)