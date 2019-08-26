from django.urls import reverse
from django.views.generic import TemplateView, ListView, View, DetailView
from .models import Slider
from django.contrib.auth.mixins import LoginRequiredMixin


class SliderListView(LoginRequiredMixin, ListView):
    template_name = 'slider/list.html'
    model = Slider
    context_object_name = 'sliders'


class SliderCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'slider/create.html'


class SliderUpdateView(LoginRequiredMixin, DetailView):
    template_name = 'slider/update.html'
    model = Slider
    context_object_name = 'slider'
