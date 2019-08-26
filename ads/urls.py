from django.urls import path
from ads import views

urlpatterns = [
    path('list/', views.AdsListView.as_view(), name='ads-list'),
    path('create/', views.AdsCreateView.as_view(), name='ads-create'),
    path('update/<int:pk>', views.AdsUpdateView.as_view(), name='ads-update'),
]
