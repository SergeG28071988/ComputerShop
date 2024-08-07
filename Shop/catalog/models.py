from django.db import models

# Create your models here.


class Component(models.Model):
    objects = None
    name = models.CharField(max_length=100, help_text="Введите товар", verbose_name="Товар")
    description = models.TextField(help_text="Введите описание товара", verbose_name="Описание товара")
    date_created = models.DateField(help_text='Введите дату добавления', verbose_name='Дата добавления')
    CATEGORY_CHOICES = [
        ('Процессоры', 'Процессоры'),
        ('Материнские платы', 'Материнские платы'),
        ('Видеокарты', 'Видеокарты'),
        ('Оперативная память', 'Оперативная память'),
        ('SSD-диски', 'SSD-диски'),
        ('HDD-диски', 'HDD-диски'),
        ('Блоки питания>', 'Блоки питания'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name='Категория')

    price = models.DecimalField(help_text="Введите цену товара", verbose_name="Цена товара", max_digits=10,
                                decimal_places=2)
    photo = models.ImageField(upload_to='images',
                              help_text="Введите фото",
                              verbose_name="Фото товара",
                              null=True, blank=True)


    def __str__(self):
        return f'Наименование: {self.name} Описание: {self.description}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
