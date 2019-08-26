from django.urls import path
from service import views

urlpatterns = [
    path('list/', views.ServiceListView.as_view(), name='service-list'),
    path('create/', views.ServiceCreateView.as_view(), name='service-create'),
    path('update/<int:pk>', views.ServiceUpdateView.as_view(), name='service-update'),
]
