# Generated by Django 4.0.1 on 2022-01-30 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_bugs_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugs',
            name='bug_title',
            field=models.TextField(default='', max_length=1500),
        ),
    ]