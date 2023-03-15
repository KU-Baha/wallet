from django.contrib import admin
from .models import Account, Tag, Category, ChildCategory, Transaction, Image

admin.site.register(Account)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(ChildCategory)
admin.site.register(Transaction)
admin.site.register(Image)