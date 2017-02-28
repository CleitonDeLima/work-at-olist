import uuid

from django.db import models
from django.utils.translation import ugettext as _
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Channel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,
                            editable=False, unique=True)
    name = models.CharField(_('name'), max_length=40, unique=True)

    class Meta:
        verbose_name = _('channel')
        verbose_name_plural = _('channels')

    def __str__(self):
        return self.name


class Category(MPTTModel):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,
                            editable=False, unique=True)

    name = models.CharField(_('name'), max_length=40)

    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='children', db_index=True)

    channel = models.ForeignKey('Channel', verbose_name=_('channel'), related_name='categories')

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.name
