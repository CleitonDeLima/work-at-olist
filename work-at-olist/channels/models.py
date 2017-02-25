import uuid

from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Channel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,
                            editable=False, unique=True)
    name = models.CharField('name', max_length=40)

    def __str__(self):
        return self.name


class Category(MPTTModel):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,
                            editable=False, unique=True)

    name = models.CharField('name', max_length=40)

    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='children', db_index=True)

    channel = models.ForeignKey('Channel', verbose_name='channel', related_name='categories')

    def __str__(self):
        return self.name
