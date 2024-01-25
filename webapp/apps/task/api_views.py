from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from rest_framework import status
from rest_framework.response import Response


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        obj = Task()
        request.data["employee_id"] = request.data["employee"]
        response = obj.create_task(request.data)
        return Response(response, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        obj = Task()
        search = request.query_params.get('search', '')
        response = obj.list_tasks(search)
        return Response(response, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        obj = Task()
        response = obj.retrieve_task(kwargs["pk"])
        return Response(response, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        obj = Task()
        request.data["id"] = kwargs["pk"]
        response = obj.update_task(request.data)
        return Response(response, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        obj = Task()
        response = obj.delete_task(kwargs["pk"])
        return Response(response, status=status.HTTP_204_NO_CONTENT)
