from django.urls import path
from document import views

urlpatterns = [
    path('list/', views.DocumentListView.as_view(), name='document-list'),
    path('create/', views.DocumentCreateView.as_view(), name='document-create'),
    path('update/<int:pk>', views.DocumentUpdateView.as_view(), name='document-update'),
]
