from django.contrib import admin
from .models import AutoMark, AutoPartCategory, AutoPart
from orders.models import Order

admin.site.site_header = 'NukusAvto'


@admin.register(AutoMark)
class AutoMarkAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(AutoPartCategory)
class AutoPartCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(AutoPart)
class AutoPartAdmin(admin.ModelAdmin):
    list_display = ['name', 'auto_mark', 'auto_part_category']
    list_filter = ['auto_mark', 'auto_part_category']
