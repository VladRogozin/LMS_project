from datetime import datetime

from django.db import models


class Student(models.Model):
    first_name = models.CharField(
        max_length=50,
        verbose_name='First name',
        db_column='f_name'
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name='Last name',
        db_column='l_name'
    )
    birthday = models.DateField(default='2003-01-01')
    city = models.CharField(max_length=50, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'students'
