# Generated by Django 4.0.1 on 2022-01-30 01:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0008_userdetail_delete_users_rename_teams_bugs_reporter_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bugs',
            name='date_created',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='bugs',
            name='date_updated',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='userdetail',
            name='access_level',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userdetail',
            name='is_dev',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userdetail',
            name='is_user',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='bugs',
            name='bug',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='bugs',
            name='reporter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bugs',
            name='visiblity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterModelTable(
            name='userdetail',
            table='details ',
        ),
    ]
