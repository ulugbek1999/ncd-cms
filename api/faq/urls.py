from django.urls import path

from api.faq.views import FaqCategoryCreate, FaqCategoryDelete, FaqCategoryUpdate, FaqCreate, FaqUpdate, FaqDelete

urlpatterns = [
    path('create/', FaqCreate.as_view(), name='faq-create-api'),
    path('delete/<int:id>', FaqDelete.as_view(), name='faq-delete-api'),
    path('update/<int:id>', FaqUpdate.as_view(), name='faq-update-api'),
    path('category/create/', FaqCategoryCreate.as_view(), name='faq-category-create-api'),
    path('category/delete/<int:id>', FaqCategoryDelete.as_view(), name='faq-category-delete-api'),
    path('category/update/<int:id>', FaqCategoryUpdate.as_view(), name='faq-category-update-api'),
]
