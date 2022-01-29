from django.contrib import admin
from base.models import bugs, users, messages, teams, softwares

# Register your models here.
admin.site.register(users)
admin.site.register(bugs)
admin.site.register(messages)
admin.site.register(teams)
admin.site.register(softwares)

