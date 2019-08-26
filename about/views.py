from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, View, DetailView
from .models import About


class AboutListView(ListView):
    template_name = 'about/list.html'
    model = About
    context_object_name = 'abouts'


class AboutCreateView(TemplateView):
    template_name = 'about/create.html'


class AboutUpdateView(DetailView):
    template_name = 'about/update.html'
    model = About
    context_object_name = 'about'
