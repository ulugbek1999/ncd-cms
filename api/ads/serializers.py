from rest_framework.serializers import ModelSerializer
from ads.models import AdsBlock, AdsBlockImage


class AdsBlockImageSerializer(ModelSerializer):
    class Meta:
        model = AdsBlockImage
        fields = ('image',)


class AdsBlockSerializer(ModelSerializer):
    block_image = AdsBlockImageSerializer(many=True, read_only=True)

    class Meta:
        model = AdsBlock
        fields = (
            'name',
            'size',
            'block_image'
        )

    def create(self, validated_data):
        instance = AdsBlock(**validated_data)
        instance.save()

        request = self.context['request']

        images = request.FILES.getlist('images')
        if images:
            for i in images:
                AdsBlockImage.objects.create(image=i, block=instance)

        # edu = super().create(validated_data)
        # if self.initial_data.getlist('docs'):
        #     for file_item in self.initial_data.getlist('docs'):
        #         file = Document(document=file_item, edu=edu)
        #         file.save()
        return instance

    def update(self, instance, validated_data):
        request = self.context['request']
        images = request.FILES.getlist('images')
        if images:
            for i in images:
                AdsBlockImage.objects.create(image=i, block=instance)
        return super().update(instance, validated_data)
