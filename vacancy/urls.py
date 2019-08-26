from django.urls import path

from .views import VacancyListView, VacancyCreateView, VacancyUpdateView

urlpatterns = [
    path('list/', VacancyListView.as_view(), name="vacancy-list"),
    path('create/', VacancyCreateView.as_view(), name="vacancy-create"),
    path('update/<int:pk>/', VacancyUpdateView.as_view(), name="vacancy-update")
]
