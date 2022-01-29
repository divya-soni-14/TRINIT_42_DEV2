from uuid import uuid4
from django.db import models

class bugs(models.Model):
    UID = models.UUIDField(default=uuid4, editable=False)
    bug = models.TextField()
    mids = models.TextField()
    reporter = models.TextField()
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