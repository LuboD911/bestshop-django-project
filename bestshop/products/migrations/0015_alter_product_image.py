# Generated by Django 3.2.5 on 2021-08-12 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='image.png', upload_to='products'),
        ),
    ]
