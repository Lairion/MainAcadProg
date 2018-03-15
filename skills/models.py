# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Skill(models.Model):
	"""docstring for Skills"""
	name = models.CharField(max_length=100)
	exp = models.IntegerField()
	image = models.ImageField(
		upload_to='uploads/%Y/%m/%d/',
		null=True,
		blank=True)
	def __str__(self):
		return str(self.name)

class Project(models.Model):
    """
    Description: Model Description
    """
    STATE = (('FH','Finish'),('InP','In Progress'),)
    name = models.CharField(max_length=100)
    description = models.TextField()
    state = models.CharField(max_length=100,choices=STATE,default="FH")
    image = models.ImageField(
		upload_to='project/%Y/%m/%d/',
		null=True,
		blank=True)
    members = models.ManyToManyField('Members')
    def __str__(self):
		return str(self.name)

class Members(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	def __str__(self):
		return str(self.first_name+' '+ self.last_name)




	

