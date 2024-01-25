import json
import os

from core.models import BaseModel
from core.utils import custom_save_image, get_unique_upload_name
from department.models import Department
from django.contrib.auth import get_user_model
from django.db import connection, models
from django.utils.translation import gettext_lazy as _

User = get_user_model()

# Create your models here.


class Designation(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Employee(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    extra_data = models.JSONField(
        null=True, blank=True, help_text="Additional data related to employee if needed"
    )

    def __str__(self):
        return f"{self.user} | {self.designation}"

    def to_dict(self, row):
        try:
            return json.loads(row)
        except TypeError:
            return {"detail": "not found"}

    def create_employee(self, data):
        result = []
        with connection.cursor() as cursor:
            query = f"""
                    SELECT public.employee_employee_create(
                        '{data.get("username")}',
                        '{data.get("password")}',
                        '{data.get("first_name")}',
                        '{data.get("last_name")}',
                        '{data.get("email")}',
                        '{data.get("phone")}',
                        '{data.get("address")}',
                        '{data.get("role")}',
                        '{data.get("dp")}',
                        {data.get("designation")},
                        {data.get("department")}
                    )
                    """
            cursor.execute(query)
            response = cursor.fetchone()
            result.append(self.to_dict(response[0] if data else None))
        return result[0]

    def update_user_password(self, user_id, password):
        user = User.objects.get(id=user_id)
        user.set_password(password)
        user.save()

    def get_file_name(self, file):
        if file:
            upload_path = os.path.join("dp", file.name)
            file = custom_save_image(upload_path, file)
        return file

    def list_employees(self, search=""):
        result = []
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT public.employee_employee_list('{search}')")
            data = cursor.fetchall()
            for row in data:
                result.append(self.to_dict(row[0]))
        return result

    def update_employee(self, data):
        """Function of update without ORM"""
        pass

    def retrieve_employee(self, id):
        """Function of retrieve without ORM"""
        pass

    def delete_employee(self, task_id):
        """Function of delete without ORM"""
        pass


class Document(BaseModel):
    class DocType(models.TextChoices):
        PAN = "pan-card", _("Pan Card")
        VOTER = "voter-id", _("Voter Id")
        AADHAR = "aadhar-card", _("Aadhar Card")
        OTHER = "other", _("Other")

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    file = models.FileField(_("Document file"), upload_to=get_unique_upload_name)
    type = models.CharField(
        max_length=32, choices=DocType.choices, default=DocType.AADHAR
    )
    is_verified = models.BooleanField(_("Is Verified"), default=False)

    def __str__(self):
        return f"{self.employee} | {self.type}"

    def to_dict(self, row):
        try:
            return json.loads(row)
        except TypeError:
            return {"detail": "not found"}

    def get_file_name(self, file):
        if file:
            upload_path = get_unique_upload_name(self, file.name)
            file = custom_save_image(upload_path, file)
        return file

    def create_document(self, data):
        result = []
        with connection.cursor() as cursor:
            query = f"""
                    SELECT public.employee_document_create(
                        {data.get('employee_id')},
                        '{data.get('file')}',
                        '{data.get('type')}',
                        {data.get('is_verified')}
                    )
                    """
            cursor.execute(query)
            response = cursor.fetchone()
            result.append(self.to_dict(response[0] if data else None))
        return result[0]


class SalaryRecord(BaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    amount = models.CharField(_("Amount ($)"), max_length=50)
    paid_date = models.DateTimeField(auto_now=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.employee} | {self.department}"
