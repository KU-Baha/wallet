from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm


def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/')

    form = NameForm()

    return render(request, 'name.html', {'form': form})


def index_page(request):
    if request.user.is_authenticated:
        return HttpResponse(f'<h1>Hello {request.user.username}</h1>')

    return HttpResponse(f'<h1>Пожалуйста авторизуйтесь!</h1>')


def second_page(request):
    return HttpResponse(f'<h1>Вторая страница!</h1>')
