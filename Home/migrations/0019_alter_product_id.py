# Generated by Django 4.1.7 on 2023-03-19 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0018_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.TextField(primary_key=True, serialize=False, unique=True),
        ),
    ]
