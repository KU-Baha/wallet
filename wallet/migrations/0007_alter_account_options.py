# Generated by Django 4.1.7 on 2023-03-17 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0006_remove_transaction_from_account_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'Счет', 'verbose_name_plural': 'Счета'},
        ),
    ]