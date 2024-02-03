from django.contrib.auth.models import AbstractUser
from django.db import models


# Дополнение стандартной модели юзера
class User(AbstractUser):
    image = models.ImageField(upload_to='users_image', blank=True, null=True, verbose_name="Аватар")
    phone_number = models.CharField(max_length=10, blank=True, null = True)
    
    class Meta():
        db_table = 'user'
        verbose_name ='Пользователя'
        verbose_name_plural ='Пользователи'
        
    def __str__(self):
        return self.username