from django.contrib import admin
from django.utils.html import format_html

from .models import Component


# Register your models here.


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date_created', 'price', 'show_photo' )
    fields = ['name', 'description', 'date_created', 'category', ('price', 'photo', 'show_photo')]
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
