from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from vacancy.models import Vacancy

class VacancyListView(LoginRequiredMixin, ListView):
    template_name = "vacancy/list.html"
    model = Vacancy
    context_object_name = "vacancies"

class VacancyCreateView(LoginRequiredMixin, TemplateView):
    template_name = "vacancy/create.html"

    def get_queryset(self, *args, **kwargs):
        return Vacancy.objects.all()


class VacancyUpdateView(LoginRequiredMixin, DetailView):
    template_name = "vacancy/update.html"
    queryset = Vacancy.objects.all()
