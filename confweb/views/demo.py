from django.http import HttpResponse
from django.shortcuts import render


def show(request, page='show'):

    data = {'page': page}

    if request.is_ajax():
        template = 'demo/' + page + '_content.html'
    else:
        template = 'demo/' + page + '.html'

    return render(request, template, data)

