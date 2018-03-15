# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Skill, Project, Members
# Register your models here.
class SkillAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Information', {
            'fields': ('name', 'exp','image',)
        }),)

admin.site.register(Skill,SkillAdmin)

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Information', {
            'fields': ('name', 'description','image', 'state',)
        }), ('Relations', {
            'fields': ('members',)
        }))
admin.site.register(Project,ProjectAdmin)

class MembersAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Information', {
            'fields': ('first_name','last_name',)
        }),)

admin.site.register(Members,MembersAdmin)
