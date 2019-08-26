from rest_framework.serializers import ModelSerializer
from employee.models import Employee


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'name_uz',
            'name_ru',
            'name_en',
            'image',
            'status',
            'position_uz',
            'position_ru',
            'position_en',
        )
