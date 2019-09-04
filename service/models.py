from django.db import models


class Service(models.Model):
    title_uz = models.TextField(blank=True, default='')
    title_ru = models.TextField(blank=True, default='')
    title_en = models.TextField(blank=True, default='')
    title_kz = models.TextField(blank=True, default='')
    short_content_uz = models.TextField(blank=True, default='')
    short_content_ru = models.TextField(blank=True, default='')
    short_content_en = models.TextField(blank=True, default='')
    short_content_kz = models.TextField(blank=True, default='')
    content_uz = models.TextField(blank=True, default='')
    content_ru = models.TextField(blank=True, default='')
    content_en = models.TextField(blank=True, default='')
    content_kz = models.TextField(blank=True, default='')
    image = models.FileField(blank=True, upload_to='cms/service/')
    status = models.BooleanField(default=True)
    slug = models.SlugField(max_length=50, default='', blank=True)

    class Meta:
        db_table = 'cms_service'
        ordering = ('-id',)

    def __str__(self):
        return self.title_ru or self.title_en or self.title_uz or self.title_kz or 'asd'
