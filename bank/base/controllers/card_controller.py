import datetime

from ..models import Account
from ..models import Card
from .charge_controller import ChargeController
from .payment_controller import PaymentController
from typing import Union
from django.db.models import Q

class CardController:

    @staticmethod
    def create_card(account: Account, name: str, cvv: str):
        card = Card.objects.create(account_number=account, name=name, cvv=cvv)
        card.save()
        return card

    @staticmethod
    def get_card_by_id(id: int):
        try:
            return Card.objects.get(id=id)
        except Card.DoesNotExist:
            return None

    @staticmethod
    def get_cards_list(query:str):
        return Card.objects.filter(Q(name__contains=query) | Q(cvv__contains=query))

    @staticmethod
    def get_card_by_account_id(account_id: int) -> Union[Card, None]:
        try:
            return Card.objects.get(account_id=account_id)
        except Card.DoesNotExist:
            return None

    @staticmethod
    def update_cvv(card_id: int, cvv: str) -> bool:
        card = Card.objects.get(id=card_id)
        card.cvv = cvv
        card.save()
        return card

    @staticmethod
    def delete_card(id: int):
        card = Card.objects.get(id=id)
        print(f'card id {card.id}')
        print(f'card account number {card.account_number}')
        account = Account.objects.get(account_number=card.account_number)
        balance = account.balance
        if balance == 0:
            card.delete()
        else:
            raise RuntimeError('Balance must be zero to delete this card')