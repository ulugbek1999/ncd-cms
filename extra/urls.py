from django.urls import path
from extra import views

urlpatterns = [
    path('list/', views.ExtraListView.as_view(), name='extra-list'),
    path('create/', views.ExtraCreateView.as_view(), name='extra-create'),
    path('update/<int:pk>', views.ExtraUpdateView.as_view(), name='extra-update'),
]
