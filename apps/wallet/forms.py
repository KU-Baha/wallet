from django import forms

from apps.wallet.models import Category, Account, Transaction, Tag, Image


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('name', 'balance',)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'type',)


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('account', 'category', 'tags', 'description', 'amount',)


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)
