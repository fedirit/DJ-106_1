# from django.http import HttpResponse
# from django.shortcuts import render, reverse
#
#
# def home_view(request):
#     template_name = 'app/home.html'
#     # впишите правильные адреса страниц, используя
#     # функцию `reverse`
#     pages = {
#         'Главная страница': reverse('home'),
#         'Показать текущее время': '',
#         'Показать содержимое рабочей директории': ''
#     }
#
#     # context и параметры render менять не нужно
#     # подбробнее о них мы поговорим на следующих лекциях
#     context = {
#         'pages': pages
#     }
#     return render(request, template_name, context)
#
#
# def time_view(request):
#     # обратите внимание – здесь HTML шаблона нет,
#     # возвращается просто текст
#     current_time = None
#     msg = f'Текущее время: {current_time}'
#     return HttpResponse(msg)
#
#
# def workdir_view(request):
#     # по аналогии с `time_view`, напишите код,
#     # который возвращает список файлов в рабочей
#     # директории
#     raise NotImplemented

import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse("time"),
        'Показать содержимое рабочей директории': reverse("workdir")
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет,
    # возвращается просто текст
    current_time = datetime.datetime.now().time()
    msg_time = f'Текущее время: {current_time}'
    return HttpResponse(msg_time)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей
    # директории
    list_directory_elemtnts = []
    path = '.'
    result_file_list = os.listdir(path)
    for file_element in result_file_list:
        list_directory_elemtnts.append(f'{file_element}, ')
    return HttpResponse(list_directory_elemtnts)
    raise NotImplemented
