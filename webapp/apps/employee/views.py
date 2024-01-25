from django.shortcuts import render
from django.views.generic import ListView
from .models import Employee

# Create your views here.


class EmployeeListView(ListView):
    model = Employee
    template_name = "employee/list.html"

    def get(self, request, *args, **kwargs):
        obj = self.model()
        search = request.GET.get('search', '')
        context = {"employee_list": obj.list_employees(search)}
        return render(request, "employee/list.html", context)
