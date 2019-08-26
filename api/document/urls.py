from django.urls import path

from api.document.views import DocumentCreate, DocumentDelete, DocumentUpdate

urlpatterns = [
    path('create/', DocumentCreate.as_view(), name='document-create-api'),
    path('delete/<int:id>', DocumentDelete.as_view(), name='document-delete-api'),
    path('update/<int:id>', DocumentUpdate.as_view(), name='document-update-api'),
]
