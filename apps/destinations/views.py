# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..users.models import User
from models import Travel, TravelManager
from django.db.models import Q

# Create your views here.
def index(request):
    if 'destination' in request.session :
        request.session.pop('destination')
    if 'description' in request.session :
        request.session.pop('description')
    if 'start' in request.session :
        request.session.pop('start')
    if 'end' in request.session :
        request.session.pop('end')
    user = User.objects.filter(id=request.session['current_user'])[0]
    travels = Travel.objects.filter(Q(creator=user) | Q(users=user)).distinct()
    other_travels = Travel.objects.all().exclude(Q(creator=user) | Q(users=user)).distinct()
    context = {
        'user' : user,
        'travels' : travels,
        'other_travels' : other_travels

    }

    return render(request, 'destinations/index.html', context)

def new(request):



    return render(request, 'destinations/new.html')

def create(request):
    if 'destination' in request.session :
        request.session.pop('destination')
    if 'description' in request.session :
        request.session.pop('description')
    if 'start' in request.session :
        request.session.pop('start')
    if 'end' in request.session :
        request.session.pop('end')
    errors = Travel.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            request.session[tag] = error
        return redirect('/travels/new')
    else:
        user = User.objects.filter(id=request.session['current_user'])[0]
        travel = Travel.objects.create(destination=request.POST['destination'], desc=request.POST['desc'], start=request.POST['start'], end=request.POST['end'], creator=user)
        travel.save()
        
        return redirect('/travels')

def show(request, id):
    travel = Travel.objects.filter(id=id)[0]
    users = travel.users.all()
    context = {
        'travel' : travel,
        'users' : users
    }
    return render(request, 'destinations/show.html', context)

def update(request, id):
    user = User.objects.filter(id=request.session['current_user'])[0]
    travel = Travel.objects.filter(id=id)[0]
    travel.users.add(user)
    travel.save()

    return redirect('/travels')