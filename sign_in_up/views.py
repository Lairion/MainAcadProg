# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User



# Create your views here.

class SignViews(object):
    
    @staticmethod
    def my_auth(request):
        username = request.POST.get('username',"user")
        password = request.POST.get('password',"....")
        user = authenticate(request, username=username, password=password)

        print(user)
        if user is not None:
            login(request, user)
            return redirect("skills:my_skill")
        else:
            # Return an 'invalid login' error message.
            return redirect('sign:in')

    @staticmethod
    def my_login(request):
        context = {
            'title':"Login"
        }
        return render(request,'login.html',context)

    @staticmethod
    def my_sign_up(request):
        context = {
            'title':'Sign up'
        }
        return render(request,'sign_up.html', context)

    @staticmethod
    def register(request):
        username = request.POST.get('username',False)
        password = request.POST.get('password',False)
        comf_pass = request.POST.get('comf_pass',False)
        email = request.POST.get('comf_pass',False)
        if username and password and comf_pass and  email:
            if password == comf_pass:
                user = User.objects.create_user(
                    username,
                    password,
                    email)
                return redirect("sign:in")
        return redirect("sign:up")

        