from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from edu.models import Edu
from about.models import About
from document.models import Document
from employee.models import Employee
from faq.models import Faq, FaqCategory
from feedback.models import Feedback
from partner.models import Partner
from service.models import Service
from django.utils.text import slugify
from settings import settings


# @receiver(pre_save, sender=Edu)
# def create_edu(sender, instance, **kwargs):
#     for word, initial in settings.REF_UTF.items():
#         instance.content_uz = instance.content_uz.replace(word, initial)


@receiver(post_save, sender=Edu)
def create_edu_slug(instance, **kwargs):
    if not instance.slug:
        if instance.title_ru:
            instance.slug = slugify(instance.title_ru, allow_unicode=True)+str(instance.id)
        else:
            instance.slug = slugify(instance.title_en)+str(instance.id)
        instance.save()


@receiver(post_save, sender=About)
def create_about_slug(instance, **kwargs):
    if not instance.slug:
        if instance.title_ru:
            instance.slug = slugify(instance.title_ru, allow_unicode=True)+str(instance.id)
        else:
            instance.slug = slugify(instance.title_en)+str(instance.id)
        instance.save()


@receiver(post_save, sender=Document)
def create_document_slug(instance, **kwargs):
    if not instance.slug:
        if instance.name_ru:
            instance.slug = slugify(instance.name_ru, allow_unicode=True)+str(instance.id)
        else:
            instance.slug = slugify(instance.name_en)+str(instance.id)
        instance.save()


@receiver(post_save, sender=Employee)
def create_employee_slug(instance, **kwargs):
    if not instance.slug:
        if instance.name_ru:
            instance.slug = slugify(instance.name_ru, allow_unicode=True)+str(instance.id)
        else:
            instance.slug = slugify(instance.name_en)+str(instance.id)
        instance.save()


@receiver(post_save, sender=Faq)
def create_faq_slug(instance, **kwargs):
    if not instance.slug:
        if instance.question_ru:
            instance.slug = slugify(instance.question_ru, allow_unicode=True)+str(instance.id)
        else:
            instance.slug = slugify(instance.question_en)+str(instance.id)
        instance.save()


@receiver(post_save, sender=Feedback)
def create_feedback_slug(instance, **kwargs):
    if not instance.slug:
        if instance.name_ru:
            instance.slug = slugify(instance.name_ru, allow_unicode=True)+str(instance.id)
        else:
            instance.slug = slugify(instance.name_en)+str(instance.id)
        instance.save()


@receiver(post_save, sender=Partner)
def create_partner_slug(instance, **kwargs):
    if not instance.slug:
        if instance.title_ru:
            instance.slug = slugify(instance.title_ru, allow_unicode=True)+str(instance.id)
        else:
            instance.slug = slugify(instance.title_en)+str(instance.id)
        instance.save()


@receiver(post_save, sender=Service)
def create_service_slug(instance, **kwargs):
    if not instance.slug:
        if instance.title_ru:
            instance.slug = slugify(instance.title_ru, allow_unicode=True)+str(instance.id)
        else:
            instance.slug = slugify(instance.title_en)+str(instance.id)
        instance.save()


@receiver(post_save, sender=FaqCategory)
def create_faq_category_slug(instance, **kwargs):
    if not instance.slug:
        if instance.name_ru:
            instance.slug = slugify(instance.name_ru, allow_unicode=True)+str(instance.id)
        else:
            instance.slug = slugify(instance.name_en)+str(instance.id)
        instance.save()
