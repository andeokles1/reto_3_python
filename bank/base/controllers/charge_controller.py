import datetime
from ..models import Account
from ..models import User
from ..models import Card
from ..models import Charge
from .account_controller import AccountController
from typing import Union, List
from django.db.models import Q

class ChargeController:

    @staticmethod
    def get_charges_list(query:str):
        return Charge.objects.filter(Q(id__contains=query) | Q(date_time__contains=query) )

    @staticmethod
    def make_a_charge(card: Card, date_time: datetime.datetime, amount: float):
        print(f'Card id {card.id}')
        print(f'Account id {card.account_number}')
        account = AccountController.get_account_by_number(account_number=card.account_number)

        if amount > 0:
            card_id = card.id
            charge = Charge.objects.create(card_id=card, date_time=date_time, amount=amount)
            AccountController.update_balance(account=account, amount=-amount)
            charge.save()
            return charge
        else:
            raise RuntimeError("Invalid amount")

    @staticmethod
    def get_charge_id(id: int) -> Union[Charge, None]:
        try:
            return Charge.objects.get(id=id)
        except Charge.DoesNotExist:
            raise RuntimeError(f'Charge with id {id} does not exist')

    @staticmethod
    def delete_charge(id:int):
        charge = ChargeController.get_charge_id(id=id)
        charge.delete()


