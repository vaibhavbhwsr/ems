from django.contrib import admin
from employee.models import Designation, Employee, Document, SalaryRecord

# Register your models here.

admin.site.register(Designation)
admin.site.register(Employee)
admin.site.register(Document)
admin.site.register(SalaryRecord)
