from django.db import models


class Country(models.Model):
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    score = models.IntegerField(default=0, blank=True)

    class Meta:
        db_table = 'directory_country'
        ordering = ['-id', ]


class EducationType(models.Model):
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    score = models.IntegerField(default=0, blank=True)

    class Meta:
        db_table = 'directory_education_type'
        ordering = ['-id', ]


class Language(models.Model):
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    excellent = models.IntegerField(default=0, blank=True)
    good = models.IntegerField(default=0, blank=True)
    not_bad = models.IntegerField(default=0, blank=True)

    class Meta:
        db_table = 'directory_language'
        ordering = ['-id', ]


class City(models.Model):
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    code = models.CharField(max_length=255)

    class Meta:
        db_table = 'directory_city'
        ordering = ['-id', ]


class District(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='district')
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)

    class Meta:
        db_table = 'directory_district'
        ordering = ['-id', ]
