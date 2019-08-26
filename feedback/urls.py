from django.urls import path
from feedback import views

urlpatterns = [
    path('list/', views.FeedbackListView.as_view(), name='feedback-list'),
    path('create/', views.FeedbackCreateView.as_view(), name='feedback-create'),
    path('update/<int:pk>', views.FeedbackUpdateView.as_view(), name='feedback-update'),
]
