# Generated by Django 4.1.2 on 2023-08-24 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_account_card_charge_payment_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='open_date',
            field=models.DateTimeField(),
        ),
    ]
