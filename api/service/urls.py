from django.urls import path

from api.service.views import ServiceCreate, ServiceDelete, ServiceUpdate

urlpatterns = [
    path('create/', ServiceCreate.as_view(), name='service-create-api'),
    path('delete/<int:id>', ServiceDelete.as_view(), name='service-delete-api'),
    path('update/<int:id>', ServiceUpdate.as_view(), name='service-update-api'),
]
