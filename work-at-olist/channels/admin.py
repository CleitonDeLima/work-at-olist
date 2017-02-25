from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Channel, Category


admin.site.register(Channel)
admin.site.register(Category, MPTTModelAdmin)
