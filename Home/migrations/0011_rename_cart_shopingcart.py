# Generated by Django 4.1.7 on 2023-03-16 07:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Home', '0010_alter_cart_product_alter_cart_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cart',
            new_name='shopingCart',
        ),
    ]
