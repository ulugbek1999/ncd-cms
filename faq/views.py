from django.urls import reverse
from django.views.generic import TemplateView, ListView, View, DetailView
from .models import Faq, FaqCategory
from django.contrib.auth.mixins import LoginRequiredMixin


class FaqListView(LoginRequiredMixin, ListView):
    template_name = 'faq/list.html'
    context_object_name = 'faqs'

    def get_queryset(self):
        return Faq.objects.filter(category__id=self.kwargs['pk'])


class FaqCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'faq/create.html'

    def get_context_data(self, **kwargs):
        context = super(FaqCreateView, self).get_context_data(**kwargs)
        context['categories'] = FaqCategory.objects.all()
        return context


class FaqUpdateView(LoginRequiredMixin, DetailView):
    template_name = 'faq/update.html'
    model = Faq
    context_object_name = 'faq'

    def get_context_data(self, **kwargs):
        context = super(FaqUpdateView, self).get_context_data(**kwargs)
        context['categories'] = FaqCategory.objects.all()
        return context


class FaqCategoryListView(LoginRequiredMixin, ListView):
    template_name = 'faq/faq_category/list.html'
    model = FaqCategory
    context_object_name = 'faq_categories'


class FaqCategoryCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'faq/faq_category/create.html'


class FaqCategoryUpdateView(LoginRequiredMixin, DetailView):
    template_name = 'faq/faq_category/update.html'
    model = FaqCategory
    context_object_name = 'faq_category'
