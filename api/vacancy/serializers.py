from rest_framework import serializers
from vacancy.models import Vacancy

class VacancySerializer(serializers.ModelSerializer):

    class Meta:
        model = Vacancy
        fields = (
            'title_en',
            'title_uz',
            'title_kz',
            'title_ru',
            'short_description_en',
            'short_description_uz',
            'short_description_kz',
            'short_description_ru',
            'description_en',
            'description_uz',
            'description_kz',
            'description_ru',
            'image',
            'location_en',
            'location_uz',
            'location_kz',
            'location_ru',
            'wages_en',
            'wages_uz',
            'wages_kz',
            'wages_ru',
            'created',
            'status',
        )

    def create(self, validated_data):
        ''' Function for creating a new 'Vacancy' instance with request information received '''
        return Vacancy.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        ''' Function for updating an existing 'Vacancy' instance with request information received '''
        instance.title_en = validated_data.get('title_en', instance.title_en)
        instance.title_uz = validated_data.get('title_uz', instance.title_uz)
        instance.title_ru = validated_data.get('title_ru', instance.title_ru)
        instance.title_kz = validated_data.get('title_kz', instance.title_kz)

        instance.short_description_en = validated_data.get('short_description_en', instance.short_description_en)
        instance.short_description_uz = validated_data.get('short_description_uz', instance.short_description_uz)
        instance.short_description_ru = validated_data.get('short_description_ru', instance.short_description_ru)
        instance.short_description_kz = validated_data.get('short_description_kz', instance.short_description_kz)

        instance.description_kz = validated_data.get('description_kz', instance.description_kz)
        instance.description_uz = validated_data.get('description_uz', instance.description_uz)
        instance.description_ru = validated_data.get('description_ru', instance.description_ru)
        instance.description_en = validated_data.get('description_en', instance.description_en)

        instance.image = validated_data.get('image', instance.image)
        instance.location_en = validated_data.get('location_en', instance.location_en)
        instance.location_uz = validated_data.get('location_uz', instance.location_uz)
        instance.location_kz = validated_data.get('location_kz', instance.location_kz)
        instance.location_ru = validated_data.get('location_ru', instance.location_ru)

        instance.wages_en = validated_data.get('wages_en', instance.wages_en)
        instance.wages_uz = validated_data.get('wages_uz', instance.wages_uz)
        instance.wages_kz = validated_data.get('wages_kz', instance.wages_kz)
        instance.wages_ru = validated_data.get('wages_ru', instance.wages_ru)
        
        instance.created = validated_data.get('created', instance.created)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance