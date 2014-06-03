# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Rooms.date'
        db.add_column(u'work_task_rooms', 'date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 6, 3, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Rooms.date'
        db.delete_column(u'work_task_rooms', 'date')


    models = {
        u'work_task.rooms': {
            'Meta': {'object_name': 'Rooms'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'spots': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'work_task.users': {
            'Meta': {'object_name': 'Users'},
            'date_joined': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'paycheck': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['work_task']