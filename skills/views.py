# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import Skill,Project

# Create your views here.
class SkillsViews(object):
	"""docstring for SkillsViews"""
	@staticmethod
	def skills(request):
		skills = Skill.objects.all()
		print(request.user)
		print(request.user.is_staff)
		context = {
			"title":"Skills",
			"skills":skills
			}
		return render(request,"skills.html",context)
	
	@staticmethod
	def show_projects(request):
		projects = Project.objects.all()
		new_projects = []
		for i in range(len(projects)):
			new_projects.append({"instance":projects[i],"result":i % 2 == 0})
		print(new_projects[0]['instance'].get_url())

		context ={
			"title":"Projects",
			"projects": new_projects

		}
		return render(request, "projects.html",context)
	@staticmethod
	def get_project(request,id):
		project = Project.objects.get(id=int(id))
		context ={
			"title":"Project",
			"project": project

		}
		
		return render(request, "project.html",context)

	@staticmethod
	def form_sessions(request):
		context = {
			'title':'examp'
		}
		return render(request,"sessions_example.html",context)

	@staticmethod
	def add_sessions(request):
		print(request.session['some_text'])
		leadboard = request.session.get("leadboard",[])
		leadboard += [{'name':request.GET.get("name",""),"score":0}]
		request.session.update({"leadboard":leadboard})

		return redirect("skills:form")

[{'name':'peter',"score":0}] + [{'name':'peter',"score":0}] == [{'name':'peter',"score":0},{'name':'peter',"score":0}] 
