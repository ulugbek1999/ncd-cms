from rest_framework.serializers import ModelSerializer
from edu.models import Document, Edu


class EduSerializer(ModelSerializer):
    class Meta:
        model = Edu
        fields = (
            'title_uz',
            'title_ru',
            'title_en',
            'short_content_uz',
            'short_content_ru',
            'short_content_en',
            'content_uz',
            'content_en',
            'content_ru',
            'status',
            'image',
            )

    def create(self, validated_data):
        instance = Edu(**validated_data)
        instance.save()

        request = self.context['request']

        docs = request.FILES.getlist('docs')
        if docs:
            for i in docs:
                Document.objects.create(document=i, edu=instance)

        # edu = super().create(validated_data)
        # if self.initial_data.getlist('docs'):
        #     for file_item in self.initial_data.getlist('docs'):
        #         file = Document(document=file_item, edu=edu)
        #         file.save()
        return instance

    def update(self, instance, validated_data):
        request = self.context['request']
        docs = request.FILES.getlist('docs')
        if docs:
            for i in docs:
                Document.objects.create(document=i, edu=instance)
        return super().update(instance, validated_data)
