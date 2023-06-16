from django.contrib import admin

from orders.models import Order, OrderAutoPart


class OrderAutoPart(admin.TabularInline):
    model = OrderAutoPart
    extra = 0
    fields = ['auto_part', 'quantity']
    readonly_fields = ['auto_part', 'quantity']
    can_delete = False


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'date', 'need_moderation']
    inlines = [OrderAutoPart]
