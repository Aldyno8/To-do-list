from django.db import models
from datetime import datetime, timedelta, date
from django.utils.formats import date_format
from django.utils.html import format_html


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    closed = models.BooleanField(default=False)
    due_date = models.DateField(null=True)
    schedule_date = models.DateField(default=datetime.now()+timedelta(days=7))

    def __str__(self):
        return self.name

