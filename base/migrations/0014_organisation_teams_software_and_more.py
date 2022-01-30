# Generated by Django 4.0.1 on 2022-01-30 02:48

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_bugs_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=50)),
                ('software_ids', models.TextField()),
            ],
            options={
                'db_table': 'organisations',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='teams',
            name='software',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.softwares'),
        ),
        migrations.AlterField(
            model_name='softwares',
            name='organisation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.organisation'),
        ),
    ]
