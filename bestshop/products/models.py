from django.contrib.auth import get_user_model
from django.db import models

from bestshop.validators.validators import validate_price

UserModel = get_user_model()

class Product(models.Model):
    title = models.CharField(
        max_length=25,
    )

    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[validate_price]
    )

    image = models.ImageField(
        default='image.png',
        upload_to='products',
        blank=True,

    )


    description = models.TextField(
        max_length=155,
    )

# тука правя да не е задължителна стойност за да мога да си направя тестовете без да създавам user
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

class Comment(models.Model):
    text = models.TextField(
        max_length=50,
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
