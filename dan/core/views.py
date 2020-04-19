from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def index(request):
    test_1 = 111
    test_2 = 222
    template = loader.get_template('index.html')
    context = {
        'test_1': test_1,
        'test_2': test_2,
    }
    return HttpResponse(template.render(context, request))
