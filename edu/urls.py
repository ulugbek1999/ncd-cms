from django.urls import path
from edu import views

urlpatterns = [
    path('list/', views.EduListView.as_view(), name='edu-list'),
    path('create/', views.EduCreateView.as_view(), name='edu-create'),
    path('update/<int:pk>', views.EduUpdateView.as_view(), name='edu-update'),
]
