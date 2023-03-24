from django.http import HttpResponse
from django.shortcuts import render

from .forms import AccountForm, CategoryForm, TagForm, TransactionForm, ImageForm
from .models import Account


def index_page(request):
    return render(request, 'wallet/index.html')


def account_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AccountForm(request.POST)

            if form.is_valid():
                account = form.save(commit=False)
                account.owner = request.user
                account.save()

        form = AccountForm()

        accounts = Account.objects.filter(owner=request.user)

        context = {
            'form': form,
            'title': 'Создать новый счет',
            'accounts': accounts
        }

        return render(request, 'wallet/account_form.html', context)

    return HttpResponse('<h1>Войдите!</h1>')


def category_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CategoryForm(request.POST)

            if form.is_valid():
                category = form.save(commit=False)
                category.owner = request.user
                category.save()

        form = CategoryForm()

        context = {
            'form': form,
            'title': 'Создать новую категорию',
        }

        return render(request, 'wallet/form.html', context)

    return HttpResponse('<h1>Войдите!</h1>')
