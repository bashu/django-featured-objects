from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

import swapper


class Featured(models.Model):
    content_object = GenericForeignKey()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    category = models.ForeignKey(swapper.get_model_name('featured', 'Category'), on_delete=models.CASCADE)
    object_id = models.IntegerField()

    def __unicode__(self):
        return ('%s' % self.pk)


class Category(models.Model):
    slug = models.SlugField(unique=True)
    active = models.BooleanField(default=False)

    class Meta:
        swappable = swapper.swappable_setting('featured', 'Category')

    def __unicode__(self):
        return self.slug


def get_featured_queryset_for(model, category=None, manager=None):
    ct = ContentType.objects.get_for_model(model)
    queryset = Featured.objects.filter(content_type=ct)
    if category:
        queryset = queryset.filter(category=category)
    if not manager:
        manager = model.objects
    return manager.filter(pk__in=queryset.values_list('object_id', flat=True))
