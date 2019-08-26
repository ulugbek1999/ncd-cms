from django.db import models


class AdsBlock(models.Model):
    name = models.TextField(default='', blank=True)
    size = models.TextField(default='2', blank=True)

    class Meta:
        db_table = 'cms_ads_blocks'
        ordering = ('id',)

    def __str__(self):
        return self.name


class AdsBlockImage(models.Model):
    image = models.FileField(upload_to='cms/ads/', blank=True)
    block = models.ForeignKey(AdsBlock, on_delete=models.CASCADE, blank=True)

    class Meta:
        db_table = 'cms_ads_block_images'
        ordering = ('id',)

    def __str__(self):
        return self.name
