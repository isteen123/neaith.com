# Generated by Django 4.1.7 on 2023-03-09 11:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('product_id', models.TextField(primary_key=True, serialize=False)),
                ('product_name', models.TextField(blank=True, max_length=25, null=True)),
                ('profile_photo', models.ImageField(blank=True, upload_to='images')),
                ('description', models.TextField(blank=True, max_length=100, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('off', models.IntegerField(blank=True, null=True)),
                ('availability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.availability')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.buyer')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.category')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.color')),
                ('posted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.size')),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(blank=True, null=True, upload_to='')),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.product')),
            ],
        ),
    ]
