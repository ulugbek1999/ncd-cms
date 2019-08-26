from django.urls import reverse
from django.views.generic import TemplateView, ListView, View, DetailView
from .models import Service
from django.contrib.auth.mixins import LoginRequiredMixin


class ServiceListView(LoginRequiredMixin, ListView):
    template_name = 'service/list.html'
    model = Service
    context_object_name = 'services'


class ServiceCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'service/create.html'


class ServiceUpdateView(LoginRequiredMixin, DetailView):
    template_name = 'service/update.html'
    model = Service
    context_object_name = 'service'
