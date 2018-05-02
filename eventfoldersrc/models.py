from django.db import models

# Create your models here.

class Venue(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	image_url = models.CharField(max_length=100)
	city = models.CharField(max_length=30)
	address = models.CharField(max_length=60)
	contact_num = models.CharField(max_length=60)
	capacity = models.CharField(max_length=100)
	rates = models.CharField(max_length=100)
	website = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Catering(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	image_url = models.CharField(max_length=100)
	city = models.CharField(max_length=30)
	address = models.CharField(max_length=60)
	contact_num = models.CharField(max_length=60)
	rates = models.CharField(max_length=100)
	website = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class LightsAndSounds(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	image_url = models.CharField(max_length=100)
	city = models.CharField(max_length=30)
	address = models.CharField(max_length=60)
	contact_num = models.CharField(max_length=60)
	rates = models.CharField(max_length=100)
	website = models.CharField(max_length=100)

	def __str__(self):
		return self.name