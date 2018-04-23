# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
import bcrypt
from models import *

# Create your views here.
def index(request) :

    return render(request, 'users/index.html')
   
def register(request) :
    if 'name' in request.session :
        request.session.pop('name')
    if 'alias' in request.session :
        request.session.pop('alias')
    if 'email' in request.session :
        request.session.pop('email')
    if 'password' in request.session :
        request.session.pop('password')
    if 'confirmation' in request.session :
        request.session.pop('confirmation')
    if 'lemail' in request.session :
        request.session.pop('lemail')
    if 'lpassword' in request.session :
        request.session.pop('lpassword')
    errors = User.objects.register_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            request.session[tag] = error
        return redirect('/')
    else:
        password = bcrypt.hashpw('test'.encode(), bcrypt.gensalt())
        user = User.objects.create(name=request.POST['name'], alias=request.POST['alias'], email=request.POST['email'], password=password)
        user.save()
        request.session['current_user'] = User.objects.filter(email=request.POST['email'])[0].id
        return redirect('/travels')

def login(request) :
    if 'name' in request.session :
        request.session.pop('name')
    if 'alias' in request.session :
        request.session.pop('alias')
    if 'email' in request.session :
        request.session.pop('email')
    if 'password' in request.session :
        request.session.pop('password')
    if 'confirmation' in request.session :
        request.session.pop('confirmation')
    if 'lemail' in request.session :
        request.session.pop('lemail')
    if 'lpassword' in request.session :
        request.session.pop('lpassword')
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            request.session[tag] = error
        return redirect('/')
    else:
        request.session['current_user'] =  User.objects.filter(email=request.POST['email'])[0].id
        return redirect('/travels')

def show(request, id):
    context = {
        'user' : User.objects.filter(id=id)[0]
    }
    return render(request, 'users/show.html', context)

def logout(request):
    request.session.clear()
    return render(request, 'users/index.html')