from django.urls import reverse
from django.views.generic import TemplateView, ListView, View, DetailView
from .models import Edu
from django.contrib.auth.mixins import LoginRequiredMixin


class EduListView(LoginRequiredMixin, ListView):
    template_name = 'edu/list.html'
    model = Edu
    context_object_name = 'edus'


class EduCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'edu/create.html'


class EduUpdateView(LoginRequiredMixin, DetailView):
    template_name = 'edu/update.html'
    model = Edu
    context_object_name = 'edu'
