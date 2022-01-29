from uuid import uuid4
from django.db import models

class users(models.Model):
    UID = models.UUIDField(default=uuid4, editable=False)
    teamids = models.TextField()
    username = models.CharField(unique= True, max_length=50)
    email = models.EmailField(unique= True, max_length=100)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    organisation = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, blank=True, null=True)
    teams = models.TextField()
    bugs = models.TextField()
    last_login = models.DateTimeField()
   
    
    class Meta:
        managed = True
        app_label = 'base'
        db_table = 'users'
        verbose_name_plural = 'users'
    
    def __str__(self):
        return self.username

    
class bugs(models.Model):
    UID = models.UUIDField(default=uuid4, editable=False)
    bug = models.TextField()
    # messages = JSONField(default = dict)
    mids = models.TextField()
    password = models.CharField(max_length=255)
    company = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    teams = models.TextField()
    tags = models.TextField()
    visiblity = models.IntegerField()
    
    class Meta:
        managed = True
        app_label = 'base'
        db_table = 'bugs'
    
   
class messages(models.Model):
    UID = models.UUIDField(default=uuid4, editable=False)
    datetime = models.DateTimeField()
    text = models.TextField()
    updoots = models.IntegerField()
    linkedto = models.TextField() # linked to a prev message with id=
    sender = models.CharField(max_length=255)

    class Meta:
        managed = True
        app_label = 'base'
        db_table = 'messages'

class teams(models.Model):
    UID = models.UUIDField(default=uuid4, editable=False)
    name = models.CharField(max_length=50)
    participantsid = models.TextField()
    lead = models.CharField(max_length=255)
    sdev = models.TextField()
    jdev = models.TextField()
    class Meta:
        managed = True
        app_label = 'base'
        db_table = 'teams'
    
    
class softwares(models.Model):
    UID = models.UUIDField(default=uuid4, editable=False)
    name = models.CharField(max_length=50)
    teamids = models.TextField()
    organisation = models.CharField(max_length=50)

    class Meta:
        managed = True
        app_label = 'base'
        db_table = 'softwares'