from django.db import models


class Country(models.Model):
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    score = models.IntegerField(default=0, blank=True)

    class Meta:
        db_table = 'directory_country'
        ordering = ['-id', ]
