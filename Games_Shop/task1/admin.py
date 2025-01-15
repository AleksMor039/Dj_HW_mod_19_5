from django.contrib import admin
from .models import Buyer, Game


# Register your models here.

# Админ панель для модели (Game)
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_filter = ('size', 'cost',)  # фильтр-ия по полям size и cost
    list_display = ('title', 'cost', 'size')  # Отображение полей title, cost и size при отображении всех полей списком
    search_fields = ('title',)  # поиск по полю title
    list_per_page = 20  # огранич.кол-ва записей


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_filter = ('balance', 'age',)  # фильтр-ия по полям balance и age
    list_display = ('name', 'balance', 'age')  # Отобр. полей name, balance и age при отображении всех полей списком
    search_fields = ('name',)  # поиск по полю name
    list_per_page = 30  # огранич.кол-ва записей
    readonly_fields = ('balance',) # только для чтения
