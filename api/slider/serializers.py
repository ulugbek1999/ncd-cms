from rest_framework.serializers import ModelSerializer
from slider.models import Slider


class SliderSerializer(ModelSerializer):
    class Meta:
        model = Slider
        fields = (
            'title_uz',
            'title_ru',
            'title_en',
            'title_kz',
            'image',
            'status',
            'content_uz',
            'content_kz',
            'content_ru',
            'content_en',
            'action_name_ru',
            'action_name_kz',
            'action_name_en',
            'action_name_uz',
            'action'
        )
