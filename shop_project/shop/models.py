from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название категории')
    image = models.ImageField(upload_to='categories/', null=True, blank=True, verbose_name='Изображение')
    slug = models.SlugField(unique=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               null=True, blank=True,
                               related_name='subcategories', verbose_name='Категория')

    def get_absolute_url(self):
        pass

    # Метод для получения картинок категорий в html
    def get_image_category(self):
        if self.image:
            return self.image.url
        else:
            return ''

    def __str__(self):
        return self.title

    def __repr__(self):  # Для отображения объектов
        return f'Категория: pk={self.pk}, title={self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название продукта')
    price = models.FloatField(verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    quantity = models.IntegerField(default=0, verbose_name='Количество на складе')
    description = models.TextField(default='Здесь скоро будит описание товара', verbose_name='Описание')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='products', verbose_name='Категория')
    slug = models.SlugField(unique=True, null=True)
    size = models.IntegerField(default=30, verbose_name='Размер')
    color = models.CharField(max_length=30, default='Серебро', verbose_name='Цвет/Материл')

    def get_absolute_url(self):
        pass

    # Метод для получения картинок категорий в html
    def get_image_product(self):
        if self.images:
            try:
                return self.images.first().image.url
            except:
                return ''
        else:
            return ''

    def __str__(self):
        return self.title

    def __repr__(self):  # Для отображения объектов
        return f'Товар: pk={self.pk}, title={self.title} price={self.price}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Gallery(models.Model):
    image = models.ImageField(upload_to='products/', verbose_name='Изображения')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name='Продукт')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    number = models.CharField(max_length=250)
    password = models.CharField(max_length=128, blank=False, default='нету пароля')

    def __str__(self):
        return self.user.username

    @classmethod
    def create_user_profile(cls, username, email, password, number):
        # Создаем пользователя с использованием предоставленных данных
        user = User.objects.create_user(username=username, email=email, password=password)
        # Создаем профиль пользователя
        user_profile = cls.objects.create(user=user, email=email, number=number)
        return user_profile
