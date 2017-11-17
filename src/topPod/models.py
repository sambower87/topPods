# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Sport(models.Model):
	name		=	models.CharField(max_length=500)
	slug		= 	models.SlugField(null=True, blank=True)
	image		=	models.ImageField(upload_to='sport_images', default = 'media/default.png')


	def __str__(self):
		return self.name

class Pod(models.Model):
	name 			=	models.CharField(max_length=500)
	description		=	models.TextField()
	sport 			= 	models.ForeignKey(Sport, related_name = 'podcasts', default=None, blank=True, null=True)
	image			=	models.ImageField(upload_to='pod_images', default = 'media/default.png')
	date_added 		= 	models.DateTimeField(auto_now_add=True)
	date_updated 	= 	models.DateTimeField(auto_now=True)
	link			= 	models.CharField(max_length=500, default=None, blank=True, null=True)

	def __str__(self):
		return self.name
