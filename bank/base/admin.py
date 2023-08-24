from django.contrib import admin
from .models import User, Account, Card, Payment, Charge
# Register your models here.

admin.site.register(User)
admin.site.register(Account)
admin.site.register(Card)
admin.site.register(Payment)
admin.site.register(Charge)
