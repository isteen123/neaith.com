# Generated by Django 4.1.7 on 2023-03-18 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0016_order_paid_order_payment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='additional_info',
            field=models.TextField(blank=True, null=True),
        ),
    ]
