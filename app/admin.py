from django.contrib import admin

from .models import Client, Product, Order


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    fields = ('name', 'email', 'phone_number', 'address', 'registration_date',)
    readonly_fields = ('registration_date',)
    list_display = ('id', 'name', 'email', 'phone_number', 'registration_date',)
    list_filter = ('registration_date',)
    search_fields = ('name', 'email', 'phone_number',)
    ordering = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'price', 'quantity', 'added_date', 'photo')
    readonly_fields = ('added_date',)
    list_display = ('id', 'name', 'price', 'quantity', 'added_date',)
    list_filter = ('added_date',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = ('client', 'products', 'total_amount', 'order_date',)
    readonly_fields = ('order_date',)
    list_display = ('id', 'client', 'total_amount', 'order_date',)
    list_filter = ('order_date',)
    search_fields = ('client__name',)
    raw_id_fields = ('client',)
    ordering = ('order_date',)
