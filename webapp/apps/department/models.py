from core.models import BaseModel
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()

# Create your models here.


class DepartmentType(models.Model):
    name = models.CharField(_("Type name"), max_length=50)
    description = models.CharField(_("Type Description"), max_length=50)

    def __str__(self):
        return f"{self.name}"


class Department(BaseModel):
    name = models.CharField(_("Name"), max_length=254)
    description = models.CharField(
        _("Description"), max_length=50, blank=True, null=True
    )
    type = models.ForeignKey(DepartmentType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} | {self.type}"
