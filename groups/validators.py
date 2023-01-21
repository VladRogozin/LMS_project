from datetime import datetime
from django.core.exceptions import ValidationError


def validate_start_date(values):
    now = datetime.now().date()
    if (now - values).days >= 0:
        raise ValidationError(f'date"{values}" is old')

