from rest_framework.serializers import ModelSerializer
from about.models import About


class AboutSerializer(ModelSerializer):
    class Meta:
        model = About
        fields = (
            'title_uz',
            'title_ru',
            'title_en',
            'content_uz',
            'content_ru',
            'content_en',
            'image',
            'status',
        )
