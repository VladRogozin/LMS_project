import datetime

from dateutil.relativedelta import relativedelta
from django.core.validators import MinLengthValidator
from django.db import models
from faker import Faker

from groups.models import Group
from students.validators import ValidateEmailDomain, validate_unique_email

VALID_DOMAINS = ('gmail.com', 'yahoo.com', 'test.com')


class Student(models.Model):
    first_name = models.CharField(
        max_length=50,
        verbose_name='First name',
        db_column='f_name',
        validators=[MinLengthValidator(3)],
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name='Last name',
        db_column='l_name'
    )
    birthday = models.DateField(default='2003-01-01')
    city = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(validators=[validate_unique_email])                                         #validators=[ValidateEmailDomain(*VALID_DOMAINS)]
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='students')
    phone = models.CharField(max_length=20, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'students'

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email}'

    def get_age(self):
        return relativedelta(datetime.date.today(), self.birthday).years

    @classmethod
    def generate_fake_data(cls, cnt):
        f = Faker()
        gro = Group.objects.all()
        for _ in range(cnt):
            s = cls()
            s.first_name = f.first_name()
            s.last_name = f.last_name()
            s.email = f'{s.first_name}.{s.last_name}@{f.random.choice(VALID_DOMAINS)}'
            s.birthday = f.date_between(start_date='-65y', end_date='-18y')
            s.age = f.random_int(min=18, max=65)
            s.group = f.random.choice(gro)
            s.save()
