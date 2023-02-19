from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'pie': {
        'мука, г': 200,
        'яйца, шт': 2,
        'сахар, г': 150,
        'яблоко, шт': 2,
    }
}


def home_view(request):
    template_name = 'apps/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
    }

    context = {
        'pages': pages
    }
    return render(request, 'home.html', context)


def time_view(request):
    current_time = datetime.datetime.now().time()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    file_lst = os.listdir(path='.')
    return HttpResponse(file_lst)


def dishes_calculator(request, dish):
    servings = request.GET.get('servings', None)
    recipe = None
    text = None
    if dish:
        if dish in DATA:
            if servings:
                servings = int(servings)
                new_recipe = {}
                for key, value in DATA[dish].items():
                    new_recipe[key] = value * servings
                recipe = new_recipe
            else:
                recipe = DATA[dish]
        else:
            text = 'Not found'
    context = {
        'recipe': recipe,
        'text': text,
    }
    return render(request, 'rec.html', context)
