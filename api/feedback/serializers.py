from rest_framework.serializers import ModelSerializer
from feedback.models import Feedback


class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = (
            'name_uz',
            'name_ru',
            'name_en',
            'short_content_uz',
            'short_content_ru',
            'short_content_en',
            'content_uz',
            'content_ru',
            'content_en',
            'image',
            'status',
            'position_uz',
            'position_ru',
            'position_en',
        )
