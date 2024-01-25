from django.contrib.auth.models import AbstractUser
from django.db import models


class NotDeleted(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(is_deleted=False)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_at = models.DateTimeField(auto_now=True, db_index=True)
    is_deleted = models.BooleanField(default=False, help_text="Used for soft delete")

    all_object = models.Manager()
    objects = NotDeleted()

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    class Meta:
        abstract = True


class User(AbstractUser):
    USER_ROLE = (
        ("Manager", "Manager"),
        ("Admin", "Admin"),
        ("Employee", "Employee"),
        ("Other", "Other"),
        ("None", None)
    )

    phone = models.CharField(max_length=32, blank=True, null=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    role = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        choices=USER_ROLE,
        default="Admin",
    )
    dp = models.ImageField(upload_to="dp/", blank=True)
