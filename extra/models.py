from django.db import models


class Extra(models.Model):
    title_uz = models.TextField(blank=True, default='')
    title_ru = models.TextField(blank=True, default='')
    title_en = models.TextField(blank=True, default='')
    short_content_ru = models.TextField(blank=True, default='')
    short_content_uz = models.TextField(blank=True, default='')
    short_content_en = models.TextField(blank=True, default='')
    content_ru = models.TextField(blank=True, default='')
    content_uz = models.TextField(blank=True, default='')
    content_en = models.TextField(blank=True, default='')

    class Meta:
        db_table = 'cms_extra'
        ordering = ('-id',)

    def __str__(self):
        return self.title_ru or self.title_en or self.title_uz or 'asd'
