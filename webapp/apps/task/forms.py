from django import forms
from .models import Task, Attachment


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "eta", "start_time", "end_time", "employee"]
        widgets = {
            "start_time": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "end_time": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }


class FileForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = ["task", "file"]
