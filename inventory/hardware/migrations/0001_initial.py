# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Item'
        db.create_table(u'hardware_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('user', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('make', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('barcode', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('serial', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('express_service_code', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('computer_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('ip_address', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39)),
            ('wireless_mac', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('swap_cycle', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('shipping_provider', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('tracking_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('stored_tracking_information', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('warranty_end', self.gf('django.db.models.fields.DateField')()),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('swap_item', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('purchased', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True)),
            ('received', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateField')()),
            ('updated_at', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'hardware', ['Item'])

        # Adding model 'PurchaseOptions'
        db.create_table(u'hardware_purchaseoptions', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('make', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created_at', self.gf('django.db.models.fields.DateField')()),
            ('updated_at', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'hardware', ['PurchaseOptions'])


    def backwards(self, orm):
        # Deleting model 'Item'
        db.delete_table(u'hardware_item')

        # Deleting model 'PurchaseOptions'
        db.delete_table(u'hardware_purchaseoptions')


    models = {
        u'hardware.item': {
            'Meta': {'object_name': 'Item'},
            'barcode': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'computer_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created_at': ('django.db.models.fields.DateField', [], {}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'express_service_code': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'make': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'purchased': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'received': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'serial': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'shipping_provider': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'stored_tracking_information': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'swap_cycle': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'swap_item': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tracking_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateField', [], {}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'warranty_end': ('django.db.models.fields.DateField', [], {}),
            'wireless_mac': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        u'hardware.purchaseoptions': {
            'Meta': {'object_name': 'PurchaseOptions'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created_at': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'make': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['hardware']