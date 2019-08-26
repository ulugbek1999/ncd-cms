from django.db import models
from django.utils.translation import get_language
from django.utils import timezone
import datetime
from django.utils.translation import ugettext_lazy as _
import pytz


utc = pytz.UTC

STATUS_CHOICES = (
    ('0', False),
    ('1', True)
)


class CommonInfo(models.Model):
    title_ru = models.CharField(_("Title (ru)"), max_length=50, default="", blank=True)
    title_en = models.CharField(_("Title (en)"), max_length=50, default="", blank=True)
    title_uz = models.CharField(_("Title (uz)"), max_length=50, default="", blank=True)
    title_kz = models.CharField(_("Title (kz)"), max_length=50, default="", blank=True)
    short_description_ru = models.CharField(_("Short description (ru)"), max_length=150, default="", blank=True)
    short_description_en = models.CharField(_("Short description (en)"), max_length=150, default="", blank=True)
    short_description_uz = models.CharField(_("Short description (uz)"), max_length=150, default="", blank=True)
    short_description_kz = models.CharField(_("Short description (kz)"), max_length=150, default="", blank=True)
    description_ru = models.TextField(default="", blank=True)
    description_en = models.TextField(default="", blank=True)
    description_uz = models.TextField(default="", blank=True)
    description_kz = models.TextField(default="", blank=True)

    class Meta:
        abstract = True


class Vacancy(CommonInfo):
    image = models.FileField(upload_to="vacancies/", blank=True)
    created = models.DateTimeField(_("Created"))
    location_ru = models.CharField(_("Location (ru)"), max_length=100)
    location_uz = models.CharField(_("Location (uz)"), max_length=50)
    location_kz = models.CharField(_("Location (kz)"), max_length=50)
    location_en = models.CharField(_("Location (en)"), max_length=50)
    wages_en = models.CharField(_("Wages (en)"), max_length=50)
    wages_ru = models.CharField(_("Wages (ru)"), max_length=50)
    wages_kz = models.CharField(_("Wages (kz)"), max_length=50)
    wages_uz = models.CharField(_("Wages (uz)"), max_length=50)
    status = models.BooleanField(_("Status"), choices=STATUS_CHOICES)

    def __str__(self):
        return self.title_en
    
    class Meta:
        db_table = "vacancy"
        verbose_name = "vacancy"
        verbose_name_plural = "vacancies"
        ordering = ['-created']