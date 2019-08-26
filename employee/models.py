from django.db import models


class Employee(models.Model):
    name_uz = models.TextField(blank=True, default='')
    name_ru = models.TextField(blank=True, default='')
    name_en = models.TextField(blank=True, default='')
    image = models.ImageField(blank=True, upload_to='cms/employee/')
    status = models.BooleanField(default=True)
    position_uz = models.TextField(blank=True, default='')
    position_en = models.TextField(blank=True, default='')
    position_ru = models.TextField(blank=True, default='')
    slug = models.SlugField(max_length=50, default='', blank=True)

    class Meta:
        db_table = 'cms_employee'
        ordering = ('-id', )

    def __str__(self):
        return self.name_ru or self.name_en or self.name_uz or 'asd'
