from django.urls import reverse
from django.views.generic import TemplateView, ListView, View, DetailView
from .models import Partner
from django.contrib.auth.mixins import LoginRequiredMixin


class PartnerListView(LoginRequiredMixin, ListView):
    template_name = 'partner/list.html'
    model = Partner
    context_object_name = 'partners'


class PartnerCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'partner/create.html'


class PartnerUpdateView(LoginRequiredMixin, DetailView):
    template_name = 'partner/update.html'
    model = Partner
    context_object_name = 'partner'
