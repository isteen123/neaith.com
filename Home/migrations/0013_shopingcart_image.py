# Generated by Django 4.1.7 on 2023-03-16 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0012_shopingcart_price_shopingcart_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopingcart',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
