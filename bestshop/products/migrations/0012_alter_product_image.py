# Generated by Django 3.2.5 on 2021-08-05 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='products'),
        ),
    ]