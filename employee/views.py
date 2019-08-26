from django.urls import reverse
from django.views.generic import TemplateView, ListView, View, DetailView
from .models import Employee
from django.contrib.auth.mixins import LoginRequiredMixin


class EmployeeListView(LoginRequiredMixin, ListView):
    template_name = 'our_employee/list.html'
    model = Employee
    context_object_name = 'employees'


class EmployeeCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'our_employee/create.html'


class EmployeeUpdateView(LoginRequiredMixin, DetailView):
    template_name = 'our_employee/update.html'
    model = Employee
    context_object_name = 'employee'
