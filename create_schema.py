#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from django.utils.encoding import smart_str, smart_unicode
import yaml
import sys
import os

def main(schema_file):
	# This function reads yaml file, creates models and registers them into admin site

	#check if we already have models file
	flag=0
	if os.path.isfile('work_task/models.py'):
		flag=1
	classes={}
	schema = yaml.load(open(schema_file))

	# Creating models in model.py
	file=open('./work_task/models.py','w')
	file.write('#!/usr/bin/env python2\n')
	file.write('# -*- coding: utf-8 -*-\n')
	file.write('from django.db import models\n')
	for class_name in schema:
		file.write(class_name.capitalize()+' = type("'+class_name.capitalize()+'",(models.Model,), {')
		for row in schema[class_name]['fields']:
			name = row['id']
			help_text = row['title']
			if row['type'] == 'char':
				file.write('"'+name+'"'+':models.CharField(max_length=100, help_text="'
					+smart_str(help_text)+'"),')
			elif row['type'] == 'int':
				file.write('"'+name+'"'+':models.IntegerField(default=0, help_text="'
					+smart_str(help_text)+'"),')
			elif row['type'] == 'date':
				file.write('"'+name+'"'+':models.DateField(help_text="'
					+smart_str(help_text)+'"),')
		file.write('"__module__":"work_task.models"})\n')
	file.close()

	#Registering models in admin.py
	file = open('./work_task/admin.py', 'w')
	file.write('from django.contrib import admin\n')
	for class_name in schema:
		file.write('from work_task.models import '+class_name.capitalize()+'\n')
		file.write('admin.site.register('+class_name.capitalize()+')\n')
	file.close()

	# Creating classes for forms.py
	file = open('./work_task/forms.py', 'w')
	file.write('#!/usr/bin/env python2\n')
	file.write('# -*- coding: utf-8 -*-\n')
	file.write('from django import forms\n')
	file.write('from work_task.models import *\n')
	file.write('from django.forms.extras.widgets import SelectDateWidget\n')
	file.write('\n')
	for class_name in schema:
		file.write('class '+class_name.capitalize()+'Form(forms.ModelForm):\n')
		for row in schema[class_name]['fields']:
			name = row['id']
			help_text = row['title']
			if row['type'] == 'char':
				file.write('    '+name+' = forms.CharField(max_length=100, help_text="'
					+smart_str(help_text)+'")\n')
			elif row['type'] == 'int':
				file.write('    '+name+' = forms.IntegerField(help_text="'
					+smart_str(help_text)+'")\n')
			elif row['type'] == 'date':
				file.write('    '+name+' = forms.DateField(widget=SelectDateWidget(), help_text="'
					+smart_str(help_text)+'")\n')
		file.write('    model_name = forms.CharField(widget=forms.TextInput(attrs={"readonly":"readonly"}), initial = "'+class_name.capitalize()+'")\n')
		file.write('    class Meta:\n        model = '+class_name.capitalize())
		file.write('\n')

	file.close()
	if flag==0:
		os.system('python manage.py schemamigration work_task --initial')
		os.system('python ./manage.py syncdb --migrate')
	else:
		os.system('python manage.py schemamigration work_task --auto')
		os.system('python manage.py migrate work_task')



if __name__=='__main__':
	# Reading name of the file
	schema_file = sys.argv[1]
	main(schema_file)