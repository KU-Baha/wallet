from django.urls import path
from .views import index_page, account_view, account_create, account_update, account_delete

urlpatterns = [
    path('', index_page, name='index'),
    path('accounts/', account_view, name='account'),
    path('account-create/', account_create, name='account-create'),
    path('account-update/<int:pk>/', account_update, name='account-update'),
    path('accounts-delete/<int:pk>/', account_delete, name='account-delete'),
    # path('category/', category_view, name='category'),
    # path('index/', index_page, name='index'),
    # path('second/', second_page),
    # path('create-account/', create_account)
]
