from rest_framework import routers
from . import api_views
from django.urls import include, path

router = routers.DefaultRouter()
router.register("employee", api_views.EmployeeViewSet, basename="employee")
router.register("document", api_views.EmployeeDocumentViewSet, basename="document")

app_name = "employee"

urlpatterns = [
    path("", include(router.urls)),
]
