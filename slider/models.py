from django.db import models


class Slider(models.Model):
    title_uz = models.TextField(blank=True, default='')
    title_en = models.TextField(blank=True, default='')
    title_ru = models.TextField(blank=True, default='')
    image = models.ImageField(blank=True, upload_to='cms/slider/')
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'cms_slider'
        ordering = ('-id',)

    def __str__(self):
        return self.title_ru or self.title_en or self.title_uz or 'asd'
