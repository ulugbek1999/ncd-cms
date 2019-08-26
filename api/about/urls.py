from django.urls import path

from api.about.views import AboutCreate, AboutDelete, AboutUpdate

urlpatterns = [
    path('create/', AboutCreate.as_view(), name='about-create-api'),
    path('delete/<int:id>', AboutDelete.as_view(), name='about-delete-api'),
    path('update/<int:id>', AboutUpdate.as_view(), name='about-update-api'),
]
