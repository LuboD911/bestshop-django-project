from django import forms
from django.core.exceptions import ValidationError


def validate_dot(value):
    if '.' in value:
        raise forms.ValidationError("'.' is present in value. You can't have dots in the title. ")



def validate_price(value):
    if value < 100:
        raise ValidationError(f"The price must be at least 100$.")