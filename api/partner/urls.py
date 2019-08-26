from django.urls import path

from api.partner.views import PartnerCreate, PartnerDelete, PartnerUpdate

urlpatterns = [
    path('create/', PartnerCreate.as_view(), name='partner-create-api'),
    path('delete/<int:id>', PartnerDelete.as_view(), name='partner-delete-api'),
    path('update/<int:id>', PartnerUpdate.as_view(), name='partner-update-api'),
]
