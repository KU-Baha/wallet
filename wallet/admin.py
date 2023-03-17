from django.contrib import admin
from .models import Account, Tag, Category, Transaction, Image


class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'name', 'balance')
    list_display_links = ('id', 'owner')
    list_filter = ('owner',)
    list_editable = ('balance', )
    search_fields = ('name', )


admin.site.register(Account, AccountAdmin)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(Image)
