import json

from core.models import BaseModel
from core.utils import get_task_upload_name
from django.db import connection, models
from django.utils.translation import gettext_lazy as _
from employee.models import Employee

# Create your models here.


class Task(BaseModel):
    class Status(models.TextChoices):
        TD = "todo", _("To Do")
        IP = "in-progress", _("In Progress")
        IR = "in-review", _("In Review")
        DONE = "done", _("Done")
        OTHER = "other", _("Other")

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True)
    description = models.TextField()
    eta = models.FloatField(
        default=0,
        help_text="Estimated Time of Arrival",
    )
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.title} | {self.employee}"

    def to_dict(self, row):
        try:
            return json.loads(row)
        except TypeError:
            return {"detail": "not found"}

    def create_task(self, data):
        result = []
        with connection.cursor() as cursor:
            query = f"""
                    SELECT public.task_task_create(
                            '{data.get('title')}',
                            '{data.get('description')}',
                            {data.get('eta')},
                            '{data.get('start_time')}',
                            '{data.get('end_time')}',
                            {data.get('employee')}
                        )
                    """
            cursor.execute(query)
            data = cursor.fetchone()
            result.append(self.to_dict(data[0] if data else None))
        return result[0]

    def update_task(self, data):
        result = []
        with connection.cursor() as cursor:
            query = f"""
                SELECT public.task_task_update(
                    {data.get("id")},
                    '{data.get("title")}',
                    '{data.get("description")}',
                    {data.get("eta")},
                    '{data.get("start_time")}',
                    '{data.get("end_time")}',
                    {data.get("employee")}
                )
            """
            cursor.execute(query)
            data = cursor.fetchone()
            result.append(self.to_dict(data[0] if data else None))
        return result[0]

    def retrieve_task(self, id):
        result = []
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT public.task_task_retrieve({id})")
            data = cursor.fetchone()
            result.append(self.to_dict(data[0] if data else None))
        return result[0]

    def list_tasks(self, search=""):
        result = []
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT public.task_task_list('{search}')")
            data = cursor.fetchall()
            for row in data:
                result.append(self.to_dict(row[0]))
        return result

    def delete_tasks(self, task_id):
        with connection.cursor() as cursor:
            cursor.execute("SELECT public.task_task_delete(%s)", (task_id,))
            result = cursor.fetchone()
        return result[0]


class Attachment(BaseModel):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    file = models.FileField(_("Task file"), upload_to=get_task_upload_name)

    def __str__(self):
        return f"{self.file}"

    def to_dict(self, row):
        try:
            return json.loads(row)
        except TypeError:
            return {"detail": "not found"}

    def create_task_attachment(self, data):
        result = []
        with connection.cursor() as cursor:
            query = f"""
                SELECT public.task_attachment_create(
                    '{data.get("file")}',
                    {data.get("task_id")}
                )
            """
            cursor.execute(query)
            data = cursor.fetchone()
            result.append(self.to_dict(data[0] if data else None))
        return result[0]

    def update_task_attachment(self, data):
        result = []
        with connection.cursor() as cursor:
            query = f"""
                SELECT public.task_attachment_update(
                    {data.get("id")},
                    '{data.get("file")}',
                    {data.get("task_id")}
                )
            """
            cursor.execute(query)
            data = cursor.fetchone()
            result.append(self.to_dict(data[0] if data else None))
        return result[0]

    def retrieve_task_attachment(self, attachment_id):
        result = []
        with connection.cursor() as cursor:
            query = f"SELECT public.task_attachment_retrieve({attachment_id})"
            cursor.execute(query)
            data = cursor.fetchone()
            result.append(self.to_dict(data[0] if data else None))
        return result[0]

    def list_task_attachments(self):
        """ "Not created stored procedure here. but can be created if needed."""
        pass

    def delete_task_attachments(self, attachment_id):
        with connection.cursor() as cursor:
            cursor.execute("SELECT public.task_attachment_delete(%s)", (attachment_id,))
            result = cursor.fetchone()
        return result[0]
