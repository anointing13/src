# Generated by Django 4.2.16 on 2024-11-05 16:23

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0011_alter_product_is_hidden'),
    ]

    operations = [
        migrations.CreateModel(
            name='HiddenProduct',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('product.product',),
        ),
    ]
