from django.core.exceptions import ValidationError
from django.test import TestCase

from bestshop.validators.validators import validate_price


class ValidatePrice(TestCase):

    def test_WhenPriceIsBiggerThan100_expectNothing(self):
        value = 150
        validate_price(value)

    def test_WhenPriceIsBiggerIs100_expectNothing(self):
        value = 100
        validate_price(value)

    def test_WhenPriceILessThan100_expectToRaise(self):
        value = 15
        with self.assertRaises(ValidationError) as context:
            validate_price(value)

        self.assertIsNotNone(context.exception)

