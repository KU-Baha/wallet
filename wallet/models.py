from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    """ Моделька счета """
    name = models.CharField('Название счета', max_length=50, default="Счет")
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Владелец')


class Tag(models.Model):
    """ Теги """
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=50)
    is_transfer = models.BooleanField(default=False)


class ChildCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Transfer(models.Model):
    from_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='from_transfers')
    to_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='to_transfers')
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    child_category = models.ForeignKey(ChildCategory, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)


class Image(models.Model):
    transfer = models.ForeignKey(Transfer, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
