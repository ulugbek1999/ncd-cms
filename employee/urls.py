from django.urls import path
from employee import views

urlpatterns = [
    path('list/', views.EmployeeListView.as_view(), name='employee-list'),
    path('create/', views.EmployeeCreateView.as_view(), name='employee-create'),
    path('update/<int:pk>', views.EmployeeUpdateView.as_view(), name='employee-update'),
]
