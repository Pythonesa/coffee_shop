from django.contrib import admin
from .models import Order, OrderItem


# Register your models here.
class OrderItemInlineAdmin(admin.TabularInline):
    model = OrderItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderItemInlineAdmin]


admin.site.register(Order, OrderAdmin)
