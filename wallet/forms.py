from django import forms

from wallet.models import Category, Account


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('name', 'balance', )
        # exclude = ('owner', )


