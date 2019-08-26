from django.db import models


class About(models.Model):
    title_uz = models.TextField(blank=True, default='')
    title_ru = models.TextField(blank=True, default='')
    title_en = models.TextField(blank=True, default='')
    content_uz = models.TextField(blank=True, default='')
    content_ru = models.TextField(blank=True, default='')
    content_en = models.TextField(blank=True, default='')
    image = models.ImageField(upload_to='cms/about/', blank=True, null=True)
    status = models.BooleanField(blank=True, default=True)
    slug = models.SlugField(max_length=50, default='', blank=True)

    class Meta:
        db_table = 'cms_about'
        ordering = ('id',)

    def __str__(self):
        return self.title_ru or self.title_en or self.title_uz or 'asd'
