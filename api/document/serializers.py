from rest_framework.serializers import ModelSerializer
from document.models import Document


class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields = (
            'name_uz',
            'name_ru',
            'name_en',
            'file',
            'status',
        )
