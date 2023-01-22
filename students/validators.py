from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def validate_unique_email(value):
    from students.models import Student
    if Student.objects.filter(email=value).exists():
        raise ValidationError(f'this email already exists {value}')


@deconstructible
class ValidateEmailDomain:
    def __init__(self, *domains):
        if domains:
            self.domains = tuple(domains)
        else:
            self.domains = DOMAINS

    def __call__(self, *args, **kwargs):
        domain = args[0].split('@')[-1]
        if domain not in self.domains:
            raise ValidationError(f'Emails domain "{domain}" is not correct')