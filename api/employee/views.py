from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from employee.models import Employee
from .serializers import EmployeeSerializer


class EmployeeCreate(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeUpdate(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_url_kwarg = 'id'


class EmployeeDelete(DestroyAPIView):
    queryset = Employee.objects.all()
    lookup_url_kwarg = 'id'
