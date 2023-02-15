from datetime import datetime

from django.db import models
from faker import Faker

from students.validators import validate_unique_email


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PersonModel(BaseModel):
    VALID_DOMAINS = ('gmail.com', 'yahoo.com', 'test.com')
    first_name = models.CharField(
        max_length=50,
        verbose_name='First name',
        db_column='f_name',
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name='Last name',
        db_column='l_name'
    )
    birthday = models.DateField(default='2023-01-01', blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(validators=[validate_unique_email])  # validators=[ValidateEmailDomain(*VALID_DOMAINS)]
    phone = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        abstract = True

    @classmethod
    def _generate(cls):
        f = Faker()

        first_name = f.first_name()
        last_name = f.last_name()
        obj = cls(
            first_name=first_name,
            last_name=last_name,
            birthday=f.date_between(start_date='-65y', end_date='-18y'),
            email=f'{first_name}{last_name}@{f.random.choice(cls.VALID_DOMAINS)}',
            city=f.city()
        )
        obj.save()

        return obj

    @classmethod
    def generator(cls, cnt):
        for _ in range(cnt):
            cls._generate()