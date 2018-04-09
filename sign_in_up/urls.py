from django.conf.urls import url
from .views import SignViews
urlpatterns = [
    url(r'^login/', SignViews.my_login, name='in'),
    url(r'^auth/', SignViews.my_auth, name='auth'),
    url(r'^sign_up/', SignViews.my_sign_up, name='up'),
    url(r'^register/', SignViews.register, name='register'),
]	#url('projects/<int:id>/',SkillsViews.get_project,name='my_project'),