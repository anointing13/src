# Generated by Django 4.2.16 on 2024-09-23 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_product_is_hidden'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_hidden',
            field=models.BooleanField(default=False),
        ),
    ]
