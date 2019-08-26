from rest_framework.serializers import ModelSerializer
from slider.models import Slider


class SliderSerializer(ModelSerializer):
    class Meta:
        model = Slider
        fields = (
            'title_uz',
            'title_ru',
            'title_en',
            'image',
            'status',
        )
