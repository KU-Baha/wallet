from django.urls import path
from .views import index_page, second_page

urlpatterns = [
    path('index/', index_page),
    path('second/', second_page)
]
