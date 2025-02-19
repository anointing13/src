# Generated by Django 4.2.16 on 2024-11-16 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_product_is_hidden'),
        ('points_wallet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.product'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='product_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('PURCHASE_BONUS', 'Purchase Bonus'), ('BIG_PURCHASE_BONUS', 'Big Purchase Bonus'), ('LOGIN_BONUS', 'Login Bonus'), ('WITHDRAWAL', 'Withdrawal'), ('PURCHASE', 'Purchase')], max_length=50),
        ),
    ]
