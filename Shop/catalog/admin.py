from django.contrib import admin
from .models import Component
from django.utils.html import format_html, mark_safe

# Register your models here.


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'show_photo')
    fields = ['name', 'description', 'category', ('price', 'photo', 'date_created', 'show_photo')]
    readonly_fields = ["show_photo"]

    def show_photo(self, obj):
        if obj.photo:
            return format_html(
                f'<img src="{obj.photo.url}" style="max-height: 100px;">')
            # можно и с использованием функции mark_safe
            # return mark_safe(
            # f'<img src="{obj.photo.url}" style="max-height: 100px;">')
        else:
            return "Фото не доступно"

    show_photo.short_description = 'Фото товара'