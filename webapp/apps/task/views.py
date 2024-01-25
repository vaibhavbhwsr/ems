from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from .models import Attachment, Task

from .forms import FileForm, TaskForm

# Create your views here.


class TaskListView(ListView):
    model = Task
    template_name = "task/list.html"

    def get(self, request, *args, **kwargs):
        obj = self.model()
        search = request.GET.get('search', '')
        context = {"task_list": obj.list_tasks(search)}
        return render(request, "task/list.html", context)


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task/add.html"
    success_url = reverse_lazy("task:task_list")

    def post(self, request, *args, **kwargs):
        obj = self.model()
        _ = obj.create_task(request.POST)
        return redirect(self.success_url)


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task/edit.html"  # Create this template
    success_url = reverse_lazy("task:task_list")

    def put(self, request, *args, **kwargs):
        obj = self.model()
        _ = obj.update_task(request.POST)
        return redirect(self.success_url)


class TaskDeleteView(View):
    model = Task

    def get(self, request, *args, **kwargs):
        obj = self.model()
        task_id = kwargs.get("pk")
        _ = obj.delete_tasks(task_id)
        return redirect("task:task_list")


class TaskRetrieveView(DetailView):
    model = Task
    template_name = "task/edit.html"


class FileCreateView(CreateView):
    model = Attachment
    form_class = FileForm
    template_name = "task/add_file.html"
    success_url = reverse_lazy("task:task_list")
