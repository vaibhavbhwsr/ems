from rest_framework import viewsets
from .models import Employee, Document
from .serializers import EmployeeSerializer, EmployeeDocumentSerializer
from rest_framework import status
from rest_framework.response import Response


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def create(self, request, *args, **kwargs):
        obj = Employee()
        request.data["dp"] = obj.get_file_name(request.data.get("dp", ""))
        response = obj.create_employee(request.data)
        if response and "user_id" in response:
            obj.update_user_password(response["user_id"], request.data["password"])
        return Response(response, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        obj = Employee()
        search = request.query_params.get("search", "")
        response = obj.list_employees(search)
        return Response(response, status=status.HTTP_200_OK)


class EmployeeDocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = EmployeeDocumentSerializer

    def create(self, request, *args, **kwargs):
        obj = Document()
        request.data["file"] = obj.get_file_name(request.data.get("file", ""))
        is_verified = request.data.get("is_verified")
        request.data["is_verified"] = (
            True if is_verified in ["true", True, 1] else False
        )
        response = obj.create_document(request.data)
        return Response(response, status=status.HTTP_201_CREATED)
