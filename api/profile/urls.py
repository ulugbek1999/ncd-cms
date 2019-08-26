from django.urls import path

from api.profile.views import UserUpdate

urlpatterns = [
    path('update/', UserUpdate.as_view(), name='profile-update-api'),
]
