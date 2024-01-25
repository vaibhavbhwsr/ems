from rest_framework import routers
from . import api_views
from django.urls import include, path

router = routers.DefaultRouter()
router.register("task", api_views.TaskViewSet, basename="task")

app_name = "task"

urlpatterns = [
    path("", include(router.urls)),
]
