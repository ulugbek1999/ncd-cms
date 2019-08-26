from django.shortcuts import render
from .models import AdsBlock
from django.views.generic import TemplateView, ListView, View, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class AdsListView(LoginRequiredMixin, ListView):
    template_name = 'ads/list.html'
    model = AdsBlock
    context_object_name = 'ads_blocks'


class AdsCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'ads/create.html'


class AdsUpdateView(LoginRequiredMixin, DetailView):
    model = AdsBlock
    template_name = 'ads/update.html'
    context_object_name = 'ads_block'
