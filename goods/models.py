from django.db import models


# Создаение таблицы с категориями товаров
class Categories(models.Model):
    # Имя категории
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    # Ссылка на категорию
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )

    # Настройка мета данных
    class Meta:
        db_table = "category"
        # Название таблицы в ед.ч.
        verbose_name = "Категорию"
        # Название таблицы в мн.ч.
        verbose_name_plural = "Категории"

    # Переопределение метода подписи
    def __str__(self):
        return self.name


# Создание таблицы с продуктами
class Products(models.Model):
    # Имя продукта
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    # Автор продукта
    author = models.CharField(max_length=150, verbose_name="Автор", default="")
    # Ссылка на категорию
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    # Описание продукта
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание товара"
    )
    # Путь ссылка на изображение
    image = models.ImageField(
        upload_to="goods_images", blank=True, null=True, verbose_name="Изображение"
    )
    # Цена товара
    price = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, verbose_name="Цена"
    )
    # Размер скидки
    discount = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, verbose_name="Скидка в %"
    )
    # Количество товара
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    # Связь категории, с удалением всех товаров при удалении категории CASCADE
    category = models.ForeignKey(
        to=Categories, on_delete=models.CASCADE, verbose_name="Категория"
    )

    # Настройка мета данных
    class Meta:
        db_table = "product"
        # Название таблицы в ед.ч.
        verbose_name = "Продукт"
        # Название таблицы в мн.ч.
        verbose_name_plural = "Продукты"
        # Стандартная сортировка
        ordering = ("id",)

    # Переопределение метода подписи
    def __str__(self):
        return self.name

    # Добавление унифицированного id
    def display_id(self):
        return f"{self.id:05}"

    # Подсчет цены со скидкой
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price
