from django.db import models


class FaqCategory(models.Model):
    name_uz = models.TextField(blank=True)
    name_en = models.TextField(blank=True)
    name_ru = models.TextField(blank=True)
    name_kz = models.TextField(blank=True)
    status = models.BooleanField(default=True)
    slug = models.SlugField(max_length=50, default='', blank=True)

    class Meta:
        db_table = 'cms_faq_category'
        ordering = ('-id',)

    def __str__(self):
        return self.name_ru or self.name_en or self.name_uz or 'asd'


class Faq(models.Model):
    question_uz = models.TextField(blank=True)
    question_ru = models.TextField(blank=True)
    question_en = models.TextField(blank=True)
    question_kz = models.TextField(blank=True)
    answer_uz = models.TextField(blank=True)
    answer_ru = models.TextField(blank=True)
    answer_en = models.TextField(blank=True)
    answer_kz = models.TextField(blank=True)
    category = models.ForeignKey(
                            FaqCategory,
                            related_name='faq',
                            on_delete=models.CASCADE,
                        )
    status = models.BooleanField(default=True)
    slug = models.SlugField(max_length=50, default='', blank=True)

    class Meta:
        db_table = 'cms_faq'
        ordering = ('-id',)

    def __str__(self):
        return self.question_ru or self.question_en or self.question_uz or self.question_kz or 'asd'
