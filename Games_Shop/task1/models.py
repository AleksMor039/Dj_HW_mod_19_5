from django.db import models


# Create your models here.

class Buyer(models.Model):  # модель представл. покупателя
    name = models.CharField(max_length=100)  # имя покупателя (username аккаунта)
    balance = models.DecimalField(max_digits=100, decimal_places=3)  # баланс
    age = models.IntegerField()  # возраст

    def __str__(self):
        return self.name


class Game(models.Model):  # модель представл. игру
    title = models.CharField(max_length=100)  # назв. игры
    cost = models.DecimalField(max_digits=100, decimal_places=3)  # цена
    size = models.DecimalField(max_digits=100, decimal_places=3)  # размер файлов игры
    description = models.TextField()  # описание
    age_limited = models.BooleanField(default=False)  # ограничение 18+
    buyer = models.ManyToManyField(Buyer, related_name='game')

    def __str__(self):
        return self.title


