from django.shortcuts import render

# Импорт модели для получения данных по категория
from goods.models import Categories


def index(request):
    context = {
        "title": "Совенок - Главная",
        "content": "Кинжный магазин",
    }
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "Совенок - О нас",
        "content": "О нас",
        "text_on_page": "Страница “О компании” нашего сайта познакомит вас с дружной командой профессионалов “Совенок”, которая на протяжении многих лет радует своих маленьких читателей замечательными книгами. Мы ценим каждого клиента и стараемся удовлетворить все ваши запросы, предлагая широкий ассортимент качественных изданий. Наша цель - помочь вам найти ту самую книгу, которую вы так долго искали.",
    }
    return render(request, "main/about.html", context)
