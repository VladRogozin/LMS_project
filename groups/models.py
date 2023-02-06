from django.db import models
from faker import Faker

from groups.validators import validate_start_date

VALID_NAME= ('Python', 'Java', 'C++')


class Group(models.Model):
    group_name = models.CharField(
        max_length=50,
        verbose_name='group name',
        db_column='g_name'
    )
    group_start = models.DateField(validators=[validate_start_date])
    group_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Grope name: {self.group_name}'

    @classmethod
    def generate_fake_data(cls, cnt):
        f = Faker()
        for _ in range(cnt):
            s = cls()
            s.group_name = f.random.choice(VALID_NAME)
            s.group_text = f.text()
            s.group_start = f.future_date()

            s.save()