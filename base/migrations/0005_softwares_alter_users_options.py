# Generated by Django 4.0.1 on 2022-01-29 14:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_teams'),
    ]

    operations = [
        migrations.CreateModel(
            name='softwares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=50)),
                ('teamids', models.TextField()),
                ('organisation', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'softwares',
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'managed': True, 'verbose_name_plural': 'users'},
        ),
    ]
