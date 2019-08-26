from django.urls import path
from partner import views

urlpatterns = [
    path('list/', views.PartnerListView.as_view(), name='partner-list'),
    path('create/', views.PartnerCreateView.as_view(), name='partner-create'),
    path('update/<int:pk>', views.PartnerUpdateView.as_view(), name='partner-update'),
]
