from django.utils import timezone
from django.core import exceptions

def validate_not_in_past(value):
    if value < timezone.now():
        raise exceptions.ValidationError("The date cannot be in the past!")
