from rest_framework.serializers import ModelSerializer
from service.models import Service


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = (
            'title_uz',
            'title_ru',
            'title_en',
            'title_kz',
            'short_content_uz',
            'short_content_ru',
            'short_content_en',
            'short_content_kz',
            'content_uz',
            'content_ru',
            'content_en',
            'content_kz',
            'image',
            'image_new',
            'status',
        )
