from django.core.exceptions import ValidationError
from django.test import TestCase

from bestshop.validators.validators import validate_dot


class ValidateDots(TestCase):

    def test_IfThereIs_aDot_expectToRaise(self):
        value = 'Name.Title.IDK'
        with self.assertRaises(ValidationError) as context:
            validate_dot(value)

        self.assertIsNotNone(context.exception)

    def test_ifThereIsNOT_aDot_expectNothing(self):
        value='value'
        validate_dot(value)
