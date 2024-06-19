# Generated by Django 5.0.6 on 2024-06-18 15:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0002_alter_car_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="drivers",
            field=models.ManyToManyField(
                related_name="cars", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
