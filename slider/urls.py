from django.urls import path
from slider import views

urlpatterns = [
    path('list/', views.SliderListView.as_view(), name='slider-list'),
    path('create/', views.SliderCreateView.as_view(), name='slider-create'),
    path('update/<int:pk>', views.SliderUpdateView.as_view(), name='slider-update'),
]
