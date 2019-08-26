from django.urls import path

from api.extra.views import ExtraCreate, ExtraDelete, ExtraUpdate

urlpatterns = [
    path('create/', ExtraCreate.as_view(), name='extra-create-api'),
    path('delete/<int:id>', ExtraDelete.as_view(), name='extra-delete-api'),
    path('update/<int:id>', ExtraUpdate.as_view(), name='extra-update-api'),
]
