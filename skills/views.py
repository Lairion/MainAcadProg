# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Skill,Project

# Create your views here.
class SkillsViews(object):
	"""docstring for SkillsViews"""
	@staticmethod
	def skills(request):
		skills = Skill.objects.all()
		context = {
			"title":"Skills",
			"skills":skills
			}
		return render(request,"skills/templates/skills.html",context)
	
	@staticmethod
	def show_projects(request):
		projects = Project.objects.all()
		new_projects = []
		for i in range(len(projects)):
			new_projects.append({"instance":projects[i],"result":i % 2 == 0})

		context ={
			"title":"Projects",
			"projects": new_projects

		}
		return render(request, "skills/templates/projects.html",context)
	@staticmethod
	def get_project(request,id):
		project = Project.objects.get(id=int(id))
		context ={
			"title":"Project",
			"project": project

		}
		
		return render(request, "skills/templates/project.html",context)


