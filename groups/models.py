from django.db import models
import datetime
from Teachers.models import Teacher
from core.models import BaseModel

from groups.validators import validate_start_date


class Group(BaseModel):
    group_name = models.CharField(
        max_length=50,
        verbose_name='group name',
        db_column='g_name'
    )
    group_start = models.DateField(default=datetime.date.today)
    group_text = models.TextField(null=True, blank=True)

    headman = models.OneToOneField(
        'students.Student', on_delete=models.SET_NULL, null=True, blank=True, related_name='headman_group'
    )
    teachers = models.ManyToManyField(to=Teacher, blank=True, related_name='groups')

    class Meta:
        db_table = 'groups'

    def __str__(self):
        return f'Grope name: {self.group_name}'

    @classmethod
    def generate_fake_data(cls):
        for name in 'Python', 'Java', 'C++', 'PM', 'QA', 'C#':
            cls.objects.create(group_name=name)