from django.db import models

from core.models import PublishedModel

class Category(PublishedModel):
    title = models.CharField('Название', max_length=256)
    slug = models.SlugField('Слаг', max_length=64, unique=True)
    output_order = models.PositiveSmallIntegerField(
        'Порядок отображения', default=100)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Topping(PublishedModel):
    title = models.CharField('Название', max_length=256,
                            help_text='Название топпинга')
    slug = models.SlugField('Слаг', max_length=64, unique=True,
                            help_text='Короткое название топпинга')

    class Meta:
        verbose_name = 'Топпинги'
        verbose_name_plural = 'Топпинги'

    def __str__(self):
        return self.title


class Wrapper(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Название',
        help_text='Уникальное название обёртки, не более 256 символов')

    class Meta:
        verbose_name = 'объект «Обёртка»'
        verbose_name_plural = 'Обёртки'

    def __str__(self):
        return self.title


class IceCream(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        related_name='ice_cream',
        null=True,
        blank=True,
        verbose_name='Обёртка'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ice_creams',
        verbose_name='Категория'
    )
    output_order = models.PositiveSmallIntegerField(
        'Порядок отображения', default=100
        )
    price = models.DecimalField(max_digits=5, decimal_places=2)
    toppings = models.ManyToManyField(Topping, verbose_name='Топпинги')
    is_on_main = models.BooleanField(default=False, verbose_name='На главную')

    empty_value_display = 'Не задано'

    class Meta:
        verbose_name = 'мороженое'
        verbose_name_plural = 'Мороженое'

    def __str__(self):
        return self.title
