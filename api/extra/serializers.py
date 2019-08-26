from rest_framework.serializers import ModelSerializer
from extra.models import Extra


class ExtraSerializer(ModelSerializer):
    class Meta:
        model = Extra
        fields = (
            'title_uz',
            'title_ru',
            'title_en',
            'content_uz',
            'content_ru',
            'content_en',
            'short_content_uz',
            'short_content_ru',
            'short_content_en',
        )
