# Generated by Django 4.0.1 on 2022-01-29 18:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_softwares_alter_users_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 29, 18, 35, 58, 636115, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
