from django.urls import path

from api.employee.views import EmployeeCreate, EmployeeDelete, EmployeeUpdate

urlpatterns = [
    path('create/', EmployeeCreate.as_view(), name='employee-create-api'),
    path('delete/<int:id>', EmployeeDelete.as_view(), name='employee-delete-api'),
    path('update/<int:id>', EmployeeUpdate.as_view(), name='employee-update-api'),
]
