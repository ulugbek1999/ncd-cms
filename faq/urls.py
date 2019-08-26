from django.urls import path
from faq import views

urlpatterns = [
    path('category/<int:pk>/list/', views.FaqListView.as_view(), name='faq-list'),
    path('create/', views.FaqCreateView.as_view(), name='faq-create'),
    path('update/<int:pk>', views.FaqUpdateView.as_view(), name='faq-update'),
    path('category/list/', views.FaqCategoryListView.as_view(), name='faq-category-list'),
    path('category/create/', views.FaqCategoryCreateView.as_view(), name='faq-category-create'),
    path('category/update/<int:pk>', views.FaqCategoryUpdateView.as_view(), name='faq-category-update'),
]
