from email.policy import default
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User



class organisation(models.Model):
    UID = models.UUIDField(default=uuid4, editable=False)
    name = models.CharField(max_length=50)
    software_ids = models.TextField()

    class Meta:
        managed = True
        app_label = "base"
        db_table = "organisations"


class softwares(models.Model):
    UID = models.UUIDField(default=uuid4, editable=False)
    organisation = models.ForeignKey(organisation, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    teamids = models.TextField()

    class Meta:
        managed = True
        app_label = "base"
        db_table = "softwares"


class teams(models.Model):
    UID = models.UUIDField(default=uuid4, editable=False)
    software = models.ForeignKey(softwares, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    participantsid = models.TextField()
    lead = models.CharField(max_length=255)
    sdev = models.TextField()
    jdev = models.TextField()

    class Meta:
        managed = True
        app_label = "base"
        db_table = "teams"


class userDetail(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    # access levels 0 - user, 1 - jr dev, 2 - sr dev, 3 - tech lead, 4 - superuser
    access_level = models.IntegerField(default=0)

    class Meta:
        managed = True
        app_label = "base"
        db_table = "details "


class bugs(models.Model):
    UID = models.UUIDField(default=uuid4, editable=False)
    title = models.TextField(max_length=500, default="")
    bug = models.TextField(max_length=500)
    mids = models.TextField()
    reporter = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    tags = models.TextField()
    # 0 - unverfied, 1 -  open, 2- assigned, 3 - resolved, 4 - closed
    status = models.CharField(max_length=10, default="0")
    # visibility matches with access level. a bug with a lower visibility can be seen by everyone on the same or higher access level
    visibility = models.IntegerField(default=0)
    is_public = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(null=True)

    class Meta:
        managed = True
        app_label = "base"
        db_table = "bugs"

    def __str__(self):
        return self.title


class messages(models.Model):
    UID = models.UUIDField(default=uuid4, editable=False)
    datetime = models.DateTimeField()
    text = models.TextField()
    updoots = models.IntegerField()
    linkedto = models.TextField()  # linked to a prev message with id=
    sender = models.CharField(max_length=255)

    class Meta:
        managed = True
        app_label = "base"
        db_table = "messages"
