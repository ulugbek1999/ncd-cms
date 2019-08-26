from django.urls import path

from api.edu.views import EduCreate, EduUpdate, EduDelete, DocumentDelete

urlpatterns = [
    path('create/', EduCreate.as_view(), name='edu-create-api'),
    path('delete/<int:id>', EduDelete.as_view(), name='edu-delete-api'),
    path('document/delete/<int:id>', DocumentDelete.as_view(), name='edu-document-delete-api'),
    path('update/<int:id>', EduUpdate.as_view(), name='edu-update-api'),
]
