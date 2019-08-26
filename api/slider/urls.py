from django.urls import path

from api.slider.views import SliderCreate, SliderDelete, SliderUpdate

urlpatterns = [
    path('create/', SliderCreate.as_view(), name='slider-create-api'),
    path('delete/<int:id>', SliderDelete.as_view(), name='slider-delete-api'),
    path('update/<int:id>', SliderUpdate.as_view(), name='slider-update-api'),
]
