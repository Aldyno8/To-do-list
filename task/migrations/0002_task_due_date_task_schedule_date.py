# Generated by Django 5.0.6 on 2024-06-07 07:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='schedule_date',
            field=models.DateField(default=datetime.datetime(2024, 6, 14, 10, 15, 46, 679572)),
        ),
    ]
