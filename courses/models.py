from django.db import models
import datetime
from core.models import BaseModel


class Course(BaseModel):
    name = models.CharField(
        max_length=50,
        verbose_name='course name',
        db_column='c_name'
    )
    course_start = models.DateField(default=datetime.date.today)
    course_text = models.TextField(null=True, blank=True)
    course_group = models.OneToOneField(
        'groups.Group',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='course_group'
    )

    class Meta:
        db_table = 'courses'

    def __str__(self):
        return f'Grope name: {self.name}'

    @classmethod
    def generate_fake_data(cls):
        for name in 'Course_1', 'Course_2', 'Course_3', 'Course_4', 'Course_5':
            cls.objects.create(name=name)