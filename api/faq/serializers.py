from rest_framework.serializers import ModelSerializer
from faq.models import Faq, FaqCategory


class FaqSerializer(ModelSerializer):
    class Meta:
        model = Faq
        fields = (
            'question_uz',
            'question_ru',
            'question_en',
            'answer_uz',
            'answer_ru',
            'answer_en',
            'status',
            )

    def create(self, validated_data):
        request = self.context['request']
        if request.POST.get('category'):
            validated_data['category'] = FaqCategory.objects.get(id=request.POST.get('category'))
        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context['request']
        if request.POST.get('category'):
            validated_data['category'] = FaqCategory.objects.get(id=request.POST.get('category'))
        else:
            validated_data['category'] = instance['category']
        return super().update(instance, validated_data)


class FaqCategorySerializer(ModelSerializer):
    class Meta:
        model = FaqCategory
        fields = (
            'name_uz',
            'name_ru',
            'name_en',
            'status',
            )
