from rest_framework.serializers import ModelSerializer
from partner.models import Partner


class PartnerSerializer(ModelSerializer):
    class Meta:
        model = Partner
        fields = (
            'title_uz',
            'title_ru',
            'title_en',
            'title_kz',
            'content_uz',
            'content_ru',
            'content_en',
            'content_kz',
            'image',
            'status',
        )
