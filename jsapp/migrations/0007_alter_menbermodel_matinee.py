# Generated by Django 3.2 on 2024-02-04 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jsapp', '0006_auto_20240204_0545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menbermodel',
            name='matinee',
            field=models.CharField(max_length=100),
        ),
    ]
