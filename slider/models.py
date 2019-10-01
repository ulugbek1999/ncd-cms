from django.db import models


class Slider(models.Model):
    title_uz = models.CharField(blank=True, max_length=50)
    title_en = models.CharField(blank=True, max_length=50)
    title_ru = models.CharField(blank=True, max_length=50)
    title_kz = models.CharField(blank=True, max_length=50)
    image = models.ImageField(blank=True, upload_to='cms/slider/')
    status = models.BooleanField(default=True)
    content_uz = models.CharField(blank=True, max_length=100)
    content_kz = models.CharField(blank=True, max_length=100)
    content_ru = models.CharField(blank=True, max_length=100)
    content_en = models.CharField(blank=True, max_length=100)
    action_name_ru = models.CharField(blank=True, max_length=20)
    action_name_uz = models.CharField(blank=True, max_length=20)
    action_name_en = models.CharField(blank=True, max_length=20)
    action_name_kz = models.CharField(blank=True, max_length=20)
    action = models.CharField(blank=True, max_length=100)

    class Meta:
        db_table = 'cms_slider'
        ordering = ('-id',)

    def __str__(self):
        return self.title_ru or 'asd'
