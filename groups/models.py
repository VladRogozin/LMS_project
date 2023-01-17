from django.db import models


class Group(models.Model):
    group_name = models.CharField(
        max_length=50,
        verbose_name='group name',
        db_column='g_name'
    )
    group_start = models.DateField()
    group_text = models.TextField(null=True, blank=True)