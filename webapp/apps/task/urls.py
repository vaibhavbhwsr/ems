from django.urls import path
from .views import (
    FileCreateView,
    TaskCreateView,
    TaskDeleteView,
    TaskListView,
    TaskUpdateView,
)

app_name = "task"

urlpatterns = [
    path("list/", TaskListView.as_view(), name="task_list"),
    path("create/", TaskCreateView.as_view(), name="task_create"),
    path("<int:pk>/edit/", TaskUpdateView.as_view(), name="task_edit"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
    path("file-create/", FileCreateView.as_view(), name="file_create"),
]
