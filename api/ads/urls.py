from django.urls import path
from api.ads.views import AdsCreate, AdsDelete, AdsUpdate, AdsImageDelete

urlpatterns = [
    path('create/', AdsCreate.as_view(), name='ads-block-create-api'),
    path('delete/<int:id>', AdsDelete.as_view(), name='ads-block-delete-api'),
    path('document/delete/<int:id>', AdsImageDelete.as_view(), name='ads-block-image-delete-api'),
    path('update/<int:id>', AdsUpdate.as_view(), name='ads-block-update-api'),
]
