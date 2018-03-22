"""Portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse

from django.contrib.auth import authenticate, login

def my_auth(request):
    username = request.POST.get('username',"user")
    
    password = request.POST.get('password',"....")
    user = authenticate(request, username=username, password=password)

    print(user)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect("/skills/")
    else:
        # Return an 'invalid login' error message.
        return HttpResponseRedirect('/login/')


def my_login(request):
    context = {
        'title':"Login"
    }
    return render(request,'templates/login.html',context)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include("skills.urls", namespace="skills")),
    url(r'^login/', my_login),
    url(r'^auth/', my_auth),
    #url(r'', include("skills.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)