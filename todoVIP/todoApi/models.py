from pickle import FALSE
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.

class Todo(models.Model):
    created_user = models.ForeignKey(User, null=True, on_delete = models.CASCADE)
    title = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=datetime.now)
    
    def __str__(self) -> str:
        return self.title


class MissionGroups(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.title


class Members(models.Model):
    ROLE =(
        ('Manager', 'Manager'),
        ('Member', 'Member'),
    )

    associate  = models.ForeignKey(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=100,null=False,choices=ROLE,default=ROLE[1][0])
    title   = models.ForeignKey(MissionGroups,on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=datetime.now)
    
    def __str__(self) -> str:
        return  self.member.username + "  -   " + self.title.title


class Mission(models.Model):
    todo = models.ForeignKey(Todo, null=False, blank=True,on_delete = models.CASCADE)
    member = models.ManyToManyField(Members, null=False)
    title = models.CharField(null=False,max_length=50)
    description = models.TextField()
    orderOfImportant = models.SmallIntegerField(null=False,unique=True)
    startDate = models.DateField(default=datetime.now)
    finishDate = models.DateField(null=False)
    complated = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title



