from django.urls import path

from api.feedback.views import FeedbackCreate, FeedbackDelete, FeedbackUpdate

urlpatterns = [
    path('create/', FeedbackCreate.as_view(), name='feedback-create-api'),
    path('delete/<int:id>', FeedbackDelete.as_view(), name='feedback-delete-api'),
    path('update/<int:id>', FeedbackUpdate.as_view(), name='feedback-update-api'),
]
