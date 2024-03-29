# Generated by Django 5.0.1 on 2024-01-25 14:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_alter_user_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Manager", "Manager"),
                    ("Admin", "Admin"),
                    ("Employee", "Employee"),
                    ("Other", "Other"),
                    ("None", None),
                ],
                default="Admin",
                max_length=200,
                null=True,
            ),
        ),
    ]
