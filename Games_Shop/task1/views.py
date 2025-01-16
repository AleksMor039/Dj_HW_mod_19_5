from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import UserRegister
from django.core.paginator import Paginator # импортировать класс пагинации
from .models import *

# Create your views here.
'''код ниже из мод_18_4(представления)'''


class Platform(TemplateView):
    template_name = 'platform.html'


class Cart(TemplateView):
    template_name = 'cart.html'


def menu(request):
    mydict_games = Game.objects.all()
    context = {
        'mydict_games': mydict_games,
    }
    return render(request, 'games.html', context)


'''код ниже из мод_18_5(представления)'''


# Create your views here.
def sign_up_by_html(request):
    info = {}  # пустой словарь

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        new_users = Buyer.objects.values_list('name', flat=True)

        if username in new_users:
            info['error'] = f"Пользователь {username} уже существует"

        elif len(password) < 8:
            info['error'] = f"Пароль должен быть не менее 8 символов"

        elif repeat_password != password:
            info['error'] = f"Пароли не совпадают"

        elif int(age) < 18:
            info['error'] = f"Вы должны быть старше 18"

        else:
            Buyer.objects.create(name=username, balance=0, age=age)
            info['text'] = f"Приветсвуем, {username}!"

    return render(request, 'registration_page.html', info)


def sign_up_by_django(request):
    info = {}  # пустой словарь

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            new_users = Buyer.objects.values_list('name', flat=True)

            if username in new_users:
                info['error'] = f"Пользователь {username} уже существует"


            elif len(password) < 8:
                info['error'] = "Пароль должен быть не менее 8 символов"


            elif repeat_password != password:
                info['error'] = "Пароли не совпадают"


            elif int(age) < 18:
                info['error'] = "Вы должны быть старше 18"


            else:
                Buyer.objects.create(name=username, balance=0, age=age)
                info['text'] = f"Приветствуем, {username}!"


    else:
        form = UserRegister()
        info['message'] = form
    return render(request, 'registration_page.html', info)


def news(request):
    news = News.object.all().order_by('date') # перемен. хранит все объекты, связан. с News + сорт. по дате
    paginator = Paginator(news, 3) # перемен. логика Paginator(ф-ия пагинации)
    page_number = request.GET.get('page') # перемен. для перемещ. по стр-цам, исп. GET-запрос, извл. параметр page
    page_object = paginator.get_page(page_number) # перемен.хранит номера страниц, обращ. к paginator - метод get_page,
    # в нём номера страниц, которые извл.из запроса пользователя
    return render(request, 'news.html', {'page_object': page_object}) # возвр. пользователю
    # запрос и шаблон + объекты которые хотим вывести на страницу