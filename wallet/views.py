from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, Http404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView

from .forms import AccountForm, CategoryForm, TagForm, TransactionForm, ImageForm
from .models import Account


def index_page(request):
    return render(request, 'wallet/index.html', {'data': 'data'})


class AccountView(View):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class AccountListView(AccountView, ListView):
    template_name = 'wallet/accounts.html'
    context_object_name = 'accounts'

    def get_queryset(self):
        return Account.objects.filter(owner=self.request.user)


class AccountCreateView(AccountView, CreateView):
    model = Account
    fields = ('name', 'balance')
    template_name = 'wallet/form.html'
    success_url = reverse_lazy('account')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


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
