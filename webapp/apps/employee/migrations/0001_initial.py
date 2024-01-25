# Generated by Django 5.0.1 on 2024-01-24 13:16

import core.utils
import django.db.models.deletion
import django.db.models.manager
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("department", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Designation",
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
                ("name", models.CharField(max_length=50, unique=True)),
                ("description", models.TextField(blank=True)),
            ],
            options={
                "abstract": False,
            },
            managers=[
                ("all_object", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="Employee",
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
                    "extra_data",
                    models.JSONField(
                        blank=True,
                        help_text="Additional data related to employee if needed",
                        null=True,
                    ),
                ),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="department.department",
                    ),
                ),
                (
                    "designation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="employee.designation",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
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
            name="Document",
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
                        upload_to=core.utils.get_unique_upload_name,
                        verbose_name="Document file",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("pan-card", "Pan Card"),
                            ("voter-id", "Voter Id"),
                            ("aadhar-card", "Aadhar Card"),
                            ("other", "Other"),
                        ],
                        default="aadhar-card",
                        max_length=32,
                    ),
                ),
                (
                    "is_verified",
                    models.BooleanField(default=False, verbose_name="Is Verified"),
                ),
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
            name="SalaryRecord",
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
                ("amount", models.CharField(max_length=50, verbose_name="Amount ($)")),
                ("paid_date", models.DateTimeField(auto_now=True)),
                ("is_paid", models.BooleanField(default=False)),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="department.department",
                    ),
                ),
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
    ]