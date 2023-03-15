from django.contrib import admin
from .models import Account, Tag, Category, ChildCategory, Transfer, Image

admin.site.register(Account)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(ChildCategory)
admin.site.register(Transfer)
admin.site.register(Image)