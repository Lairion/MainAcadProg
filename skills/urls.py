from django.conf.urls import url
from .views import SkillsViews
urlpatterns = [
    url(r'^skills/$',SkillsViews.skills,name='my_skill'),
    url(r'^projects/$',SkillsViews.show_projects,name='my_projects'),
    url(r'^projects/(?P<id>[\w-]+)/$',SkillsViews.get_project,name='my_project'),
]	#url('projects/<int:id>/',SkillsViews.get_project,name='my_project'),