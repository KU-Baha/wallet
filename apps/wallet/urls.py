from django.urls import path
from .views import AccountListView, AccountCreateView, index_page, account_update, account_delete

urlpatterns = [
    path('', index_page, name='index'),
    path('accounts/', AccountListView.as_view(), name='account'),
    path('account-create/', AccountCreateView.as_view(), name='account-create'),
    path('account-update/<int:pk>/', account_update, name='account-update'),
    path('accounts-delete/<int:pk>/', account_delete, name='account-delete'),
    # path('category/', category_view, name='category'),
    # path('index/', index_page, name='index'),
    # path('second/', second_page),
    # path('create-account/', create_account)
]
