from django.urls import reverse
from django.views.generic import TemplateView, ListView, View, DetailView
from .models import Document
from django.contrib.auth.mixins import LoginRequiredMixin


class DocumentListView(LoginRequiredMixin, ListView):
    template_name = 'document/list.html'
    model = Document
    context_object_name = 'documents'


class DocumentCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'document/create.html'


class DocumentUpdateView(LoginRequiredMixin, DetailView):
    template_name = 'document/update.html'
    model = Document
    context_object_name = 'document'
