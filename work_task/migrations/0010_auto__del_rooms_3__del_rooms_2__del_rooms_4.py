# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Rooms_3'
        db.delete_table(u'work_task_rooms_3')

        # Deleting model 'Rooms_2'
        db.delete_table(u'work_task_rooms_2')

        # Deleting model 'Rooms_4'
        db.delete_table(u'work_task_rooms_4')


    def backwards(self, orm):
        # Adding model 'Rooms_3'
        db.create_table(u'work_task_rooms_3', (
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=100)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('spots', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'work_task', ['Rooms_3'])

        # Adding model 'Rooms_2'
        db.create_table(u'work_task_rooms_2', (
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=100)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('spots', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'work_task', ['Rooms_2'])

        # Adding model 'Rooms_4'
        db.create_table(u'work_task_rooms_4', (
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=100)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('spots', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'work_task', ['Rooms_4'])


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