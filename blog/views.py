from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string


def start_page(request):
    response = render_to_string('blog/index.html')
    return HttpResponse(response)


def all_posts(request):
    return render(request, 'blog/list_detail.html')


def info_name(request, строка: str):
    return render(request, 'blog/detail_by_name.html', {"строка": строка})


def info_number(request, номер: int):
    return render(request, 'blog/detail_by_number.html', {"номер": номер})


def post_about_keanu(request):
    data = {
        "year_born": '1964 г.',
        'city_born': 'Бейрут',
        'movie_name': 'На гребне волны',
    }
    return render(request, 'blog/keanu_rivs.html', context=data)


def post_about_guinness(request):
    context = {
        'power_man': 'Narve Laeret',
        'bar_name': 'Bob’s BBQ & Grill',
        'count_needle': 1790,
    }
    return render(request, 'blog/guinnessworldrecords.html', context=context)


def people_data(request):
    people = [
        'Жукова Анна Константиновна',
        'Юлия Степановна Потапова',
        'Гущин Аполлинарий Тимурович',
        'Дорофей Ярославович Третьяков',
        'Селезнева Анна Тарасовна',
        'Федотов Симон Харлампьевич',
        'Красильникова Вера Борисовна',
        'Бажен Тихонович Костин',
        'Веселова Анжелика Тимофеевна',
        'Щербаков Самсон Феодосьевич'
    ]
    return render(request, 'blog/people.html', context={'people': people})
