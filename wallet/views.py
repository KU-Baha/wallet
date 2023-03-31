from django.shortcuts import render, get_object_or_404, redirect

from .forms import AccountForm, CategoryForm, TagForm, TransactionForm, ImageForm
from .models import Account


def index_page(request):
    return render(request, 'wallet/index.html')


def account_view(request):
    if request.user.is_authenticated:
        accounts = Account.objects.filter(owner=request.user)

        context = {
            'accounts': accounts,
            'title': 'Счета'
        }

        return render(request, 'wallet/accounts.html', context)

    return redirect('index')


def account_create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AccountForm(request.POST)

            if form.is_valid():
                account = form.save(commit=False)
                account.owner = request.user
                account.save()

            return redirect('account')

        form = AccountForm()

        accounts = Account.objects.filter(owner=request.user)

        context = {
            'form': form,
            'title': 'Создать новый счет',
            'accounts': accounts
        }

        return render(request, 'wallet/form.html', context)

    return redirect('index')


def account_update(request, pk):
    user = request.user
    account = get_object_or_404(Account, pk=pk, owner=user)

    if request.method == 'POST':
        form = AccountForm(request.POST, instance=account)

        if form.is_valid():
            form.save()

        return redirect('account')

    form = AccountForm(instance=account)

    context = {
        'form': form,
        'title': 'Редактировать счет',
    }

    return render(request, 'wallet/form.html', context)


def account_delete(request, pk):
    user = request.user
    account = get_object_or_404(Account, pk=pk, owner=user)
    account.delete()
    return redirect('account')


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

    return redirect('index')
