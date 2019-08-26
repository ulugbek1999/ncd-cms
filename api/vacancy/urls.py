from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.VacancyCreateView.as_view(), name="vacancy-create-api"),
    path('delete/', views.VacancyDeleteView.as_view(), name="vacancy-delete-api"),
    path('update/<int:pk>', views.VacancyUpdateView.as_view(), name="vacancy-update-api")
]
