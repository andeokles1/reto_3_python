from django.db import models


# Create your models here.
class User(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Account(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    account_number = models.CharField(max_length=50)
    balance = models.FloatField()
    open_date = models.DateTimeField()
    limit = models.FloatField()

    def __str__(self):
        return self.account_number


class Card(models.Model):
    account_number = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=50)
    cvv = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class Charge(models.Model):
    card_id = models.ForeignKey(Card, on_delete=models.SET_NULL, null=True, blank=True)
    date_time = models.DateField()
    amount = models.FloatField()

    def __str__(self):
        return self.id

class Payment(models.Model):
    card_id = models.ForeignKey(Card, on_delete=models.SET_NULL, null=True, blank=True)
    date_time = models.DateTimeField()
    amount = models.FloatField()

    def __str__(self):
        return self.id
