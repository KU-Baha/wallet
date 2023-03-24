from django.urls import path
from .views import index_page, account_view, category_view

urlpatterns = [
    path('', index_page, name='index'),
    path('account/', account_view, name='account'),
    # path('category/', category_view, name='category'),
    # path('index/', index_page, name='index'),
    # path('second/', second_page),
    # path('create-account/', create_account)
]
