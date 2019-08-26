from django.urls import reverse
from django.views.generic import TemplateView, ListView, View, DetailView
from .models import Extra
from django.contrib.auth.mixins import LoginRequiredMixin


class ExtraListView(LoginRequiredMixin, ListView):
    template_name = 'extra/list.html'
    model = Extra
    context_object_name = 'extras'


class ExtraCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'extra/create.html'


class ExtraUpdateView(LoginRequiredMixin, DetailView):
    template_name = 'extra/update.html'
    model = Extra
    context_object_name = 'extra'
