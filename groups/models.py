from django.db import models

from groups.validators import validate_start_date


class Group(models.Model):
    group_name = models.CharField(
        max_length=50,
        verbose_name='group name',
        db_column='g_name'
    )
    group_start = models.DateField(validators=[validate_start_date])
    group_text = models.TextField(null=True, blank=True)