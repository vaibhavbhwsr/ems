# Generated by Django 5.0.1 on 2024-01-24 14:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("department", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="department",
            name="description",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Description"
            ),
        ),
    ]
