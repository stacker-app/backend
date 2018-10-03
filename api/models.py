import datetime
from math import sqrt

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.conf import settings


# Please Visit -> https://github.com/zhilyaev/stacker/wiki/Models


class Goal(models.Model):
    name = models.fields.TextField(max_length=255)
    done = models.fields.BooleanField(blank=True, default=False)
    mark = models.fields.BooleanField(blank=True, default=False)
    deadline = models.fields.DateTimeField(default=now)
    """ 
    
    
    Auto-generate:
    ↓	↓	↓	↓
    
    
    """
    id = models.fields.AutoField(primary_key=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        # default=self.request.user,
        # see -> views.GoalView
    )
    # Auto Date
    created = models.fields.DateTimeField(auto_now_add=True)
    updated = models.fields.DateTimeField(auto_now=True)
    completed = models.fields.DateTimeField(blank=True, null=True)

    @property
    def rate(self):
        # TODO Algorithm here:
        ddl = self.deadline.timestamp()
        n = datetime.datetime.now().timestamp()
        diff = ddl - n
        mk = 100 if self.mark else 200
        c = Action.objects.filter(goal=self).count()
        r = diff * (mk - sqrt(c))
        return r

    class Meta:
        ordering = ('deadline', 'updated', 'created')


class Action(models.Model):
    name = models.fields.TextField(max_length=255)
    done = models.fields.BooleanField(blank=True, default=False)
    mark = models.fields.BooleanField(blank=True, default=False)
    repeater = models.fields.TextField(blank=True, null=True)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    deadline = models.fields.DateTimeField(default=now)
    """ 


    Auto-generate:
    ↓	↓	↓	↓


    """
    id = models.fields.AutoField(primary_key=True)
    # Auto Date
    created = models.fields.DateTimeField(auto_now_add=True)
    updated = models.fields.DateTimeField(auto_now=True)
    completed = models.fields.DateTimeField(default=now, blank=True)

    @property
    def rate(self):
        # TODO Algorithm here:
        ddl = self.deadline.timestamp()
        n = datetime.datetime.now().timestamp()
        diff = ddl - n
        mk = 100 if self.mark else 200
        r = diff * mk
        return r