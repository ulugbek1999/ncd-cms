from rest_framework.views import APIView
from .serializers import VacancySerializer
from vacancy.models import Vacancy
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.db import connection

class VacancyCreateView(APIView):
    def update_sql(self, i):
        with connection.cursor() as cursor:
            cursor.execute("UPDATE vacancy SET image='vacancies/default.jpg' WHERE id=%s", [i])
            cursor.execute("SELECT * FROM vacancy WHERE id=%s", [i])
            row = cursor.fetchone()
            print(row)
        return row


    def post(self, request, format=None):
        title_en = request.data.get("title_en")
        title_uz = request.data.get("title_uz")
        title_ru = request.data.get("title_ru")
        title_kz = request.data.get("title_kz")
        short_description_en = request.data.get("short_content_en")
        short_description_uz = request.data.get("short_content_uz")
        short_description_ru = request.data.get("short_content_ru")
        short_description_kz = request.data.get("short_description_kz")
        description_en = request.data.get("content_en")
        description_uz = request.data.get("content_uz")
        description_ru = request.data.get("content_ru")
        description_kz = request.data.get("content_kz")
        image = request.data.get("image")
        location_ru = request.data.get("location_ru")
        location_en = request.data.get("location_en")
        location_kz = request.data.get("location_kz")
        location_uz = request.data.get("location_uz")
        wages_en = request.data.get("wages_en")
        wages_ru = request.data.get("wages_ru")
        wages_kz = request.data.get("wages_kz")
        wages_uz = request.data.get("wages_uz")
        status_i = request.data.get("status")

        vacancy = Vacancy.objects.create(
            title_en=title_en,
            title_ru=title_ru,
            title_kz=title_kz,
            title_uz=title_uz,
            short_description_en=short_description_en,
            short_description_kz=short_description_kz,
            short_description_ru=short_description_ru,
            short_description_uz=short_description_uz,
            description_en=description_en,
            description_kz=description_kz,
            description_ru=description_ru,
            description_uz=description_uz,
            location_en=location_en,
            location_kz=location_kz,
            location_ru=location_ru,
            location_uz=location_uz,
            image=image,
            wages_en=wages_en,
            wages_kz=wages_kz,
            wages_ru=wages_ru,
            wages_uz=wages_uz,
            created=timezone.now(),
            status=status_i,
        )
        if image is None:
            self.update_sql(vacancy.id)
        return Response(status=status.HTTP_201_CREATED)


class VacancyDeleteView(APIView):

    def delete(self, request):
        vacancy = get_object_or_404(Vacancy, pk=request.data.get("id"))
        vacancy.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


class VacancyUpdateView(APIView):

    def put(self, request, pk):
        vacancy = Vacancy.objects.get(pk=pk)

        vacancy.title_en = request.data.get("title_en")
        vacancy.title_uz = request.data.get("title_uz")
        vacancy.title_ru = request.data.get("title_ru")
        vacancy.title_kz = request.data.get("title_kz")
        vacancy.short_description_en = request.data.get("short_content_en")
        vacancy.short_description_uz = request.data.get("short_content_uz")
        vacancy.short_description_kz = request.data.get("short_content_kz")
        vacancy.short_description_ru = request.data.get("short_content_ru")
        vacancy.description_en = request.data.get("content_en")
        vacancy.description_uz = request.data.get("content_uz")
        vacancy.description_ru = request.data.get("content_ru")
        vacancy.description_kz = request.data.get("content_kz")
        if request.data.get("changed") == "true":
            vacancy.image = request.data.get("image")
        vacancy.location_ru = request.data.get("location_ru")
        vacancy.location_en = request.data.get("location_en")
        vacancy.location_kz = request.data.get("location_kz")
        vacancy.location_uz = request.data.get("location_uz")
        vacancy.wages_en = request.data.get("wages_en")
        vacancy.wages_ru = request.data.get("wages_ru")
        vacancy.wages_kz = request.data.get("wages_kz")
        vacancy.wages_uz = request.data.get("wages_uz")
        vacancy.status = request.data.get("status")
        vacancy.save()

        return Response(status=status.HTTP_202_ACCEPTED)
