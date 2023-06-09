# Generated by Django 4.1.7 on 2023-03-16 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_rename_product_id_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='color',
            field=models.TextField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='quntity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='size',
            field=models.TextField(blank=True, max_length=25, null=True),
        ),
        migrations.RemoveField(
            model_name='cart',
            name='Product',
        ),
        migrations.AddField(
            model_name='cart',
            name='Product',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.product'),
        ),
    ]
