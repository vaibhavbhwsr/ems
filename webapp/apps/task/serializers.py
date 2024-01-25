from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "employee",
            "title",
            "description",
            "eta",
            "start_time",
            "end_time",
        ]
