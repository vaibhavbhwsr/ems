from django.contrib import admin
from department.models import DepartmentType, Department

# Register your models here.

admin.site.register(DepartmentType)
admin.site.register(Department)
