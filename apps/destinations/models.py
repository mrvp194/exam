# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
import datetime
from ..users.models import User

# Create your models here.
class TravelManager(models.Manager):
    def basic_validator(self, data):
        errors = {} 
        if len(data['destination']) < 1 :
            errors['destination'] = "Invalid Destination"          
        if len(data['desc']) <= 1 :
            errors['description'] = "Invalid Description" 
        if len(data['start']) <= 1 or len(data['end']) <= 1:
            errors['start'] = "You must enter a start or end date"
        elif datetime.datetime.strptime(data['end'], '%Y-%m-%d').date() < datetime.date.today() or datetime.datetime.strptime(data['start'], '%Y-%m-%d').date() < datetime.date.today() or datetime.datetime.strptime(data['start'], '%Y-%m-%d').date() > datetime.datetime.strptime(data['end'], '%Y-%m-%d').date():
            errors['end'] = "Invalid start or end date" 
        # elif datetime.datetime.strptime(data['start'], '%Y-%m-%d').date() > datetime.datetime.strptime(data['end'], '%Y-%m-%d').date():
        #     errors['start'] = "You can't start a trip after you end it"    
        return errors
class Travel(models.Model):
    desc = models.CharField(max_length=255)
    start = models.DateField()
    end = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    destination = models.CharField(max_length=255)
    creator = models.ForeignKey(User, related_name='creator')
    users = models.ManyToManyField(User, related_name='users')
    objects = TravelManager()

