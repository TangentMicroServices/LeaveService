from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

LEAVE_TYPES = [
	('Annual Leave', 'Annual Leave'),
	('Sick Leave', 'Sick Leave'),
	('Family Responsibility Leave', 'Family Responsibility Leave'),
	('Study Leave', 'Study Leave'),

]

LEAVE_STATUS = [
	('New', 'New'),
	('Approved', 'Approved'),
	('Declined', 'Declined'),
	('Cancelled', 'Cancelled'),
]

class LeaveApplication(models.Model):

    def __unicode__(self):
        return "%s %s %s %s" (self.user.username, self.leave_type, self.start_date, self.end_data)
    
    user = models.ForeignKey(User)
    description = models.TextField(blank=True, null=True)

    leave_type = models.CharField(choices=LEAVE_TYPES, max_length=22)
    status = models.CharField(choices=LEAVE_STATUS, max_length=22, default="New")
    start_date = models.DateField('Start Date', blank=False, null=False)
    end_date = models.DateField('End Date', blank=True, null=True)
    approved = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @staticmethod 
    def quick_create(user):

    	data = {
    		"user": user,
    		"leave_type": 'Annual Leave',
    		"status": 'New',
    		"start_date": datetime.now(),
    		"end_date": datetime.now()    			
    	}
    	return LeaveApplication.objects.create(**data)
