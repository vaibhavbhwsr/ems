# Generated by Django 5.0.1 on 2024-01-24 13:16

import core.utils
import django.db.models.deletion
import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("employee", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("modified_at", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "is_deleted",
                    models.BooleanField(
                        default=False, help_text="Used for soft delete"
                    ),
                ),
                ("title", models.CharField(max_length=50, null=True)),
                ("description", models.TextField()),
                (
                    "eta",
                    models.FloatField(default=0, help_text="Estimated Time of Arrival"),
                ),
                ("start_time", models.DateTimeField(null=True)),
                ("end_time", models.DateTimeField(null=True)),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="employee.employee",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            managers=[
                ("all_object", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="Attachment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("modified_at", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "is_deleted",
                    models.BooleanField(
                        default=False, help_text="Used for soft delete"
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        upload_to=core.utils.get_task_upload_name,
                        verbose_name="Task file",
                    ),
                ),
                (
                    "task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="task.task"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            managers=[
                ("all_object", django.db.models.manager.Manager()),
            ],
        ),
    ]
