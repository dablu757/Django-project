# Generated by Django 5.0.6 on 2024-07-10 16:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="adress",
            field=models.TextField(blank=True, null=True),
        ),
    ]
