from django.core.validators import MinLengthValidator
from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(
        max_length=50,
        verbose_name='First name',
        db_column='f_name',
        validators=[MinLengthValidator(2)],
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name='Last name',
        db_column='l_name'
    )
    birthdate = models.DateField(default='2003-01-01')
    salary = models.PositiveIntegerField()