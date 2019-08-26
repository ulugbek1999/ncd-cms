from django.db import models


class Edu(models.Model):
    title_uz = models.TextField(blank=True, default='')
    title_en = models.TextField(blank=True, default='')
    title_ru = models.TextField(blank=True, default='')
    short_content_ru = models.TextField(blank=True, default='')
    short_content_en = models.TextField(blank=True, default='')
    short_content_uz = models.TextField(blank=True, default='')
    content_ru = models.TextField(blank=True, default='')
    content_en = models.TextField(blank=True, default='')
    content_uz = models.TextField(blank=True, default='')
    image = models.ImageField(upload_to='cms/edu/', blank=True)
    status = models.BooleanField(default=True)
    slug = models.SlugField(max_length=50, default='', blank=True)

    class Meta:
        db_table = 'cms_education'
        ordering = ('-id',)

    def __str__(self):
        return self.title_ru or self.title_en or self.title_uz or 'asd'


class Document(models.Model):
    document = models.FileField(blank=True, upload_to='cms/edu/documents/')
    edu = models.ForeignKey(Edu, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cms_education_documents'
