from django.db import models

# Create your models here.

class Item(models.Model):
	department = models.CharField(max_length=50)
	location = models.CharField(blank=True, max_length=50)
	user = models.CharField(max_length=50)
	make = models.CharField(blank=True, max_length=50)
	model = models.CharField(blank=True, max_length=50)
	category = models.CharField(blank=True, max_length=50)
	barcode = models.CharField(blank=True, max_length=50)
	serial = models.CharField(max_length=100)
	express_service_code = models.CharField(blank=True, max_length=250)
	computer_name = models.CharField(max_length=50)
	ip_address = models.GenericIPAddressField()
	wireless_mac = models.CharField(blank=True, max_length=30)
	swap_cycle = models.CharField(max_length=20)
	shipping_provider = models.CharField(blank=True, max_length=100)
	tracking_url = models.URLField(blank=True)
	stored_tracking_information = models.TextField(blank=True)
	warranty_end = models.DateField(auto_now=False)
	notes = models.TextField(blank=True)
	swap_item = models.IntegerField(default=0)
	purchased = models.NullBooleanField(default=False)
	received = models.NullBooleanField(default=False)
	created_at = models.DateField(auto_now=False)
	updated_at = models.DateField(auto_now=False)

class PurchaseOptions(models.Model):
	item_id = models.IntegerField(default=0)
	make = models.CharField(blank=True, max_length=50)
	model = models.CharField(blank=True, max_length=50)
	description = models.CharField(blank=True, max_length=100)
	active = models.BooleanField(default=True)
	created_at = models.DateField(auto_now=False)
	updated_at = models.DateField(auto_now=False)
	
