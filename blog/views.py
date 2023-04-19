from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

def start_page(request):
    response = render_to_string('blog/index.html')
    return HttpResponse(response)


def all_posts(request):
    return render(request, 'blog/list_detail.html')
